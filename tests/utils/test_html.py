import json
import shutil
import subprocess
from html.parser import HTMLParser

import pytest

from altair.utils.html import spec_to_html


@pytest.fixture
def spec():
    return {
        "data": {"url": "data.json"},
        "mark": {"type": "point"},
        "encoding": {
            "x": {"field": "x", "type": "quantitative"},
            "y": {"field": "y", "type": "quantitative"},
        },
    }


@pytest.mark.parametrize("requirejs", [True, False])
@pytest.mark.parametrize("fullhtml", [True, False])
def test_spec_to_html(requirejs, fullhtml, spec):
    # We can't test that the html actually renders, but we'll test aspects of
    # it to make certain that the keywords are respected.
    vegaembed_version = "3.12"
    vegalite_version = "3.0"
    vega_version = "4.0"

    html = spec_to_html(
        spec,
        mode="vega-lite",
        requirejs=requirejs,
        fullhtml=fullhtml,
        vegalite_version=vegalite_version,
        vegaembed_version=vegaembed_version,
        vega_version=vega_version,
    )
    html = html.strip()

    if fullhtml:
        assert html.startswith("<!DOCTYPE html>")
        assert html.endswith("</html>")
    else:
        assert html.startswith("<style>")
        assert html.endswith("</script>")

    if requirejs:
        assert "require(" in html
    else:
        assert "require(" not in html

    assert f"vega-lite@{vegalite_version}" in html
    assert f"vega@{vega_version}" in html
    assert f"vega-embed@{vegaembed_version}" in html


def test_spec_to_html_olli(spec):
    html = spec_to_html(
        spec,
        mode="vega-lite",
        vegalite_version="6.0",
        vegaembed_version="7",
        vega_version="6",
        template="olli",
    )

    assert "olli@3" in html
    assert "+esm" in html
    assert "styles.css" in html
    assert "olliVis" in html
    assert "connectOlliToVegaLite" in html
    assert "withExternalStateParam" in html
    assert "looksLikeFips" in html
    assert "enrichWithUSGeo" in html
    assert "olli-adapters@" not in html


class _TopLevelElements(HTMLParser):
    """Collect the top-level elements of an HTML fragment and inline script code."""

    def __init__(self) -> None:
        super().__init__()
        self.elements: list[dict[str, str | None]] = []
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        if self._depth == 0:
            attributes = dict(attrs)
            self.elements.append(
                {"tag": tag, "id": attributes.get("id"), "src": attributes.get("src")}
            )
        self._depth += 1

    def handle_endtag(self, tag):
        self._depth -= 1

    def handle_data(self, data):
        if self._depth == 1 and self.elements[-1]["tag"] == "script":
            self.elements[-1]["code"] = (self.elements[-1].get("code") or "") + data


# Runs each inline script in order with a minimal DOM: document.currentScript
# points at the script's previous sibling, getElementById returns the first
# match like browsers do for repeated ids, and require() calls back later, after
# currentScript has been cleared. Prints which element each chart was drawn in.
_RUN_EMBED_SCRIPTS = """
const vm = require("vm");
const elements = JSON.parse(require("fs").readFileSync(0, "utf8"));
const drawn = [];
const document = {
  currentScript: null,
  getElementById: (id) => elements.find((element) => element.id === id) || null,
};
function vegaEmbed(el, spec) {
  if (typeof el === "string") el = document.getElementById(el.slice(1));
  drawn.push([spec.title, elements.indexOf(el)]);
  return Promise.resolve();
}
const context = vm.createContext({
  document,
  vegaEmbed,
  require: (deps, callback) => setTimeout(() => callback(vegaEmbed)),
  requirejs: { config() {} },
});
elements.forEach((element, i) => {
  if (element.tag !== "script" || element.src) return;
  document.currentScript = { previousElementSibling: elements[i - 1] };
  vm.runInContext(element.code, context);
  document.currentScript = null;
});
setTimeout(() => console.log(JSON.stringify(drawn)));
"""


@pytest.mark.skipif(
    shutil.which("node") is None, reason="runs the scripts with Node.js"
)
@pytest.mark.parametrize("requirejs", [False, True])
@pytest.mark.parametrize("output_divs", [("vis", "vis"), ("chart-a", "chart-b")])
def test_spec_to_html_snippets_render_into_own_div(requirejs, output_divs):
    parser = _TopLevelElements()
    for title, output_div in zip(("Chart A", "Chart B"), output_divs, strict=True):
        parser.feed(
            spec_to_html(
                {"mark": "point", "title": title},
                mode="vega-lite",
                vegalite_version="6",
                vegaembed_version="7",
                vega_version="6",
                output_div=output_div,
                fullhtml=False,
                requirejs=requirejs,
            )
        )
    divs = [i for i, element in enumerate(parser.elements) if element["tag"] == "div"]

    result = subprocess.run(
        ["node", "-e", _RUN_EMBED_SCRIPTS],
        input=json.dumps(parser.elements),
        capture_output=True,
        text=True,
        check=True,
    )

    assert json.loads(result.stdout) == [["Chart A", divs[0]], ["Chart B", divs[1]]]
