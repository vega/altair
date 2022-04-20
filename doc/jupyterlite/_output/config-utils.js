/**
 * configuration utilities for jupyter-lite
 *
 * this file may not import anything else, and exposes no API
 */

/*
 * An `index.html` should `await import('../config-utils.js')` after specifying
 * the key `script` tags...
 *
 * ```html
 *  <script id="jupyter-config-data" type="application/json" data-jupyter-lite-root="..">
 *    {}
 *  </script>
 * ```
 */
const JUPYTER_CONFIG_ID = 'jupyter-config-data';

/*
 * The JS-mangled name for `data-jupyter-lite-root`
 */
const LITE_ROOT_ATTR = 'jupyterLiteRoot';

/**
 * The well-known filename that contains `#jupyter-config-data` and other goodies
 */
const LITE_FILES = ['jupyter-lite.json', 'jupyter-lite.ipynb'];

/**
 * And this link tag, used like so to load a bundle after configuration.
 *
 * ```html
 *  <link
 *    id="jupyter-lite-main"
 *    rel="preload"
 *    href="../build/bundle.js?_=bad4a54"
 *    main="index"
 *    as="script"
 *  />
 * ```
 */
const LITE_MAIN = 'jupyter-lite-main';

/**
 * The current page, with trailing server junk stripped
 */
const HERE = `${window.location.origin}${window.location.pathname.replace(
  /(\/|\/index.html)?$/,
  ''
)}/`;

/**
 * The computed composite configuration
 */
let _JUPYTER_CONFIG;

/**
 * A handle on the config script, must exist, and will be overridden
 */
const CONFIG_SCRIPT = document.getElementById(JUPYTER_CONFIG_ID);

/**
 * The relative path to the root of this JupyterLite
 */
const RAW_LITE_ROOT = CONFIG_SCRIPT.dataset[LITE_ROOT_ATTR];

/**
 * The fully-resolved path to the root of this JupyterLite
 */
const FULL_LITE_ROOT = new URL(RAW_LITE_ROOT, HERE).toString();

/**
 * Paths that are joined with baseUrl to derive full URLs
 */
const UNPREFIXED_PATHS = ['licensesUrl', 'themesUrl'];

/* a DOM parser for reading html files */
const parser = new DOMParser();

/**
 * Merge `jupyter-config-data` on the current page with:
 * - the contents of `.jupyter-lite#/jupyter-config-data`
 * - parent documents, and their `.jupyter-lite#/jupyter-config-data`
 * ...up to `jupyter-lite-root`.
 */
async function jupyterConfigData() {
  /**
   * Return the value if already cached for some reason
   */
  if (_JUPYTER_CONFIG != null) {
    return _JUPYTER_CONFIG;
  }

  let parent = new URL(HERE).toString();
  let promises = [getPathConfig(HERE)];
  while (parent != FULL_LITE_ROOT) {
    parent = new URL('..', parent).toString();
    promises.unshift(getPathConfig(parent));
  }

  const configs = (await Promise.all(promises)).flat();

  let finalConfig = configs.reduce(mergeOneConfig);

  // apply any final patches
  finalConfig = dedupFederatedExtensions(finalConfig);

  // hoist to cache
  _JUPYTER_CONFIG = finalConfig;

  return finalConfig;
}

/**
 * Merge a new configuration on top of the existing config
 */
function mergeOneConfig(memo, config) {
  for (const [k, v] of Object.entries(config)) {
    switch (k) {
      // this list of extension names is appended
      case 'disabledExtensions':
      case 'federated_extensions':
        memo[k] = [...(memo[k] || []), ...v];
        break;
      // these `@org/pkg:plugin` are merged at the first level of values
      case 'litePluginSettings':
      case 'settingsOverrides':
        if (!memo[k]) {
          memo[k] = {};
        }
        for (const [plugin, defaults] of Object.entries(v || {})) {
          memo[k][plugin] = { ...(memo[k][plugin] || {}), ...defaults };
        }
        break;
      default:
        memo[k] = v;
    }
  }
  return memo;
}

function dedupFederatedExtensions(config) {
  const originalList = Object.keys(config || {})['federated_extensions'] || [];
  const named = {};
  for (const ext of originalList) {
    named[ext.name] = ext;
  }
  let allExtensions = [...Object.values(named)];
  allExtensions.sort((a, b) => a.name.localeCompare(b.name));
  return config;
}

/**
 * Load jupyter config data from (this) page and merge with
 * `jupyter-lite.json#jupyter-config-data`
 */
async function getPathConfig(url) {
  let promises = [getPageConfig(url)];
  for (const fileName of LITE_FILES) {
    promises.unshift(getLiteConfig(url, fileName));
  }
  return Promise.all(promises);
}

/**
 * The current normalized location
 */
function here() {
  return window.location.href.replace(/(\/|\/index.html)?$/, '/');
}

/**
 * Maybe fetch an `index.html` in this folder, which must contain the trailing slash.
 */
export async function getPageConfig(url = null) {
  let script = CONFIG_SCRIPT;

  if (url != null) {
    const text = await (await window.fetch(`${url}index.html`)).text();
    const doc = parser.parseFromString(text, 'text/html');
    script = doc.getElementById(JUPYTER_CONFIG_ID);
  }
  return fixRelativeUrls(url, JSON.parse(script.textContent));
}

/**
 * Fetch a jupyter-lite JSON or Notebook in this folder, which must contain the trailing slash.
 */
export async function getLiteConfig(url, fileName) {
  let text = '{}';
  let config = {};
  const liteUrl = `${url || HERE}${fileName}`;
  try {
    text = await (await window.fetch(liteUrl)).text();
    const json = JSON.parse(text);
    const liteConfig = fileName.endsWith('.ipynb')
      ? json['metadata']['jupyter-lite']
      : json;
    config = liteConfig[JUPYTER_CONFIG_ID] || {};
  } catch (err) {
    console.warn(`failed get ${JUPYTER_CONFIG_ID} from ${liteUrl}`);
  }
  return fixRelativeUrls(url, config);
}

export function fixRelativeUrls(url, config) {
  let urlBase = new URL(url || here()).pathname;
  for (const [k, v] of Object.entries(config)) {
    config[k] = fixOneRelativeUrl(k, v, url, urlBase);
  }
  return config;
}

export function fixOneRelativeUrl(key, value, url, urlBase) {
  if (key === 'litePluginSettings' || key === 'settingsOverrides') {
    // these are plugin id-keyed objects, fix each plugin
    return Object.entries(value || {}).reduce((m, [k, v]) => {
      m[k] = fixRelativeUrls(url, v);
      return m;
    }, {});
  } else if (
    !UNPREFIXED_PATHS.includes(key) &&
    key.endsWith('Url') &&
    value.startsWith('./')
  ) {
    // themesUrls, etc. are joined in code with baseUrl, leave as-is: otherwise, clean
    return `${urlBase}${value.slice(2)}`;
  } else if (key.endsWith('Urls') && Array.isArray(value)) {
    return value.map((v) => (v.startsWith('./') ? `${urlBase}${v.slice(2)}` : v));
  }
  return value;
}

/**
 * Update with the as-configured favicon
 */
function addFavicon(config) {
  const favicon = document.createElement('link');
  favicon.rel = 'icon';
  favicon.type = 'image/x-icon';
  favicon.href = config.faviconUrl;
  document.head.appendChild(favicon);
}

/**
 * The main entry point.
 */
async function main() {
  const config = await jupyterConfigData();
  if (config.baseUrl === new URL(here()).pathname) {
    window.location.href = config.appUrl.replace(/\/?$/, '/index.html');
    return;
  }
  // rewrite the config
  CONFIG_SCRIPT.textContent = JSON.stringify(config, null, 2);
  addFavicon(config);
  const preloader = document.getElementById(LITE_MAIN);
  const bundle = document.createElement('script');
  bundle.src = preloader.href;
  bundle.main = preloader.main;
  document.head.appendChild(bundle);
}

/**
 * TODO: consider better pattern for invocation.
 */
void main();
