# Notes for Maintainers of Altair

## Auto-generating the Python code

The core Python API for Altair can be found in the following locations:

- ``altair/vegalite/v5/schema/``

All the files within these directories are created automatically by running
the following script from the root of the repository:

```bash
$ hatch run python tools/generate_schema_wrapper.py
```

This script does a couple things:

- downloads the appropriate schema files from the specified vega-lite
  release versions & copies the JSON file to the appropriate ``schema``
  directory
- generates basic low-level schemapi wrappers from the definitions within
  the schema: this is put in the ``schema/core.py`` file
- generates a second layer of higher level wrappers for some vega-lite
  functionality; this is put in ``schema/channels.py`` and ``schema/mixins.py``

The script output is designed to be deterministic; if the vega-lite version
is not changed, then running the script should overwrite the schema wrappers
with identical copies.

## Updating the Vega-Lite version

The vega & vega-lite versions for the Python code can be updated by manually
changing the ``SCHEMA_VERSION`` definition within
``tools/generate_schema_wrapper.py``, and then re-running the script.

This will update all of the automatically-generated files in the ``schema``
directory for each version, but please note that it will *not* update other
pieces (for example, the core of the Altair API, including methods and
doc strings within ``altair/vegalite/v5/api.py``.
These additional methods have fairly good test coverage, so running the test
suite should identify any inconsistencies:
```
hatch run test
```
Generally, minor version updates (e.g. Vega-Lite 2.3->2.4) have been relatively
painless, maybe requiring the addition of a few chart methods or modification
of some docstrings.
Major version updates (e.g. Vega-Lite 1.X->2.X) have required substantial
rewrites, because the internal structure of the schema changed appreciably.

### Updating the Vega-Lite in JupyterChart
To update the Vega-Lite version used in JupyterChart, update the version in the 
esm.sh URL in `altair/jupyter/js/index.js`.

For example, to update to Vega-Lite 5.15.1, Vega 5 and Vega-Embed 6, the URL 
should be:

```javascript
import embed from "https://esm.sh/vega-embed@6?deps=vega@5&deps=vega-lite@5.15.1";
```

### Updating vl-convert version bound

When updating the version of Vega-Lite, it's important to ensure that 
[vl-convert](https://github.com/vega/vl-convert) includes support for the new Vega-Lite version. 
Check the [vl-convert releases](https://github.com/vega/vl-convert/releases) to find the minimum
version of vl-convert that includes support for the desired version of Vega-Lite (and [open
an issue](https://github.com/vega/vl-convert/issues) if this version hasn't been
included in a released yet.). Update the vl-convert version check in `altair/utils/_importers.py` 
with the new minimum required version of vl-convert.

Also, the version bound of the `vl-convert-python` package should be updated in the 
`[project.optional-dependencies]/all` dependency group in `pyproject.toml`.

## Releasing the Package

To cut a new release of Altair, follow the steps outlined in
[RELEASING.md](RELEASING.md).

## Web analytics
We use the privacy-friendly [plausible.io](https://plausible.io/) for tracking usage statistics of our documentation.
It is hosted on [https://views.scientific-python.org](https://views.scientific-python.org). To view the stats, you need an account. Ask another maintainer to invite you.