# Notes for Maintainers of Altair

## Auto-generating the Python code

The core Python API for Altair can be found in the following locations:

- ``altair/vegalite/v5/schema/``

All the files within these directories are created automatically by running
the following script:

```bash
uv run task generate-schema-wrapper
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

## Updating Vega versions
All versions are maintained in [pyproject.toml](pyproject.toml).

### Python Packages

Projects which publish a package to PyPI are listed with a version bound in one of the following tables:

- [`project.dependencies`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#dependencies-optional-dependencies): Published dependencies.
- [`project.optional-dependencies`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#dependencies-optional-dependencies): Published optional dependencies, or "extras".
- [`dependency-groups`](https://peps.python.org/pep-0735/): Local dependencies for development.

> [!NOTE]
> All are currently declared in sub-tables of `project.optional-dependencies`.

The lower version bounds defined here are reused for [altair/utils/_importers.py](altair/utils/_importers.py).

#### `vl-convert`

We need to ensure that [vl-convert](https://github.com/vega/vl-convert) includes support for the new Vega-Lite version. 
Check the [vl-convert releases](https://github.com/vega/vl-convert/releases) to find the minimum
version of `vl-convert` that includes support for the desired version of Vega-Lite (and [open
an issue](https://github.com/vega/vl-convert/issues) if this version hasn't been
included in a released yet).

### Javascript/other

Additional version constraints, including for [`Vega-Lite`](https://github.com/vega/vega-lite) itself are declared in `[tool.altair.vega]`.

Whereas the [previous dependencies](#python-packages) are used primarily at *install-time*; this group is embedded into `altair` for use at *runtime* or when [generating the python code](#auto-generating-the-python-code):

```toml
[tool.altair.vega]
vega-datasets     = "..." # https://github.com/vega/vega-datasets
vega-embed        = "..." # https://github.com/vega/vega-embed
vega-lite         = "..." # https://github.com/vega/vega-lite
```

Some examples of where these propagate to:
- [altair/jupyter/js/index.js](altair/jupyter/js/index.js)
- [altair/utils/_importers.py](altair/utils/_importers.py)
- [tools/generate_schema_wrapper.py](tools/generate_schema_wrapper.py)
- [tools/versioning.py](tools/versioning.py)
- [altair/utils/schemapi.py](https://github.com/vega/altair/blob/0e23fd33e9a755bab0ef73a856340c48c14897e6/altair/utils/schemapi.py#L1619-L1640)

> [!IMPORTANT]
> When updating **any** of these versions, be sure to [re-generate the python code](#auto-generating-the-python-code).

#### Updating the Vega-Lite version

The Vega-Lite version for the Python code propagates to `tools.generate_schema_wrapper.SCHEMA_VERSION`.

This will update all of the automatically-generated files in the ``schema``
directory for each version, but please note that it will *not* update other
pieces (for example, the core of the Altair API, including methods and
doc strings within ``altair/vegalite/v5/api.py``).
These additional methods have fairly good test coverage, so running the test
suite should identify any inconsistencies:

```bash
uv run task test
```

Generally, minor version updates (e.g. Vega-Lite 2.3->2.4) have been relatively
painless, maybe requiring the addition of a few chart methods or modification
of some docstrings.
Major version updates (e.g. Vega-Lite 1.X->2.X) have required substantial
rewrites, because the internal structure of the schema changed appreciably.

## Releasing the Package

To cut a new release of Altair, follow the steps outlined in
[RELEASING.md](RELEASING.md).

## Web analytics
We use the privacy-friendly [plausible.io](https://plausible.io/) for tracking usage statistics of our documentation.
It is hosted on [https://views.scientific-python.org](https://views.scientific-python.org). You can view the stats [here](https://views.scientific-python.org/altair-viz.github.io). To get an account to edit the settings of the web tracking, ask another maintainer.