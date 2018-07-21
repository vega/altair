# Notes for Maintainers of Altair


## Auto-generating the Python code

The core Python API for Altair can be found in the following locations:

- ``altair/vegalite/v2/schema/``
- ``altair/vegalite/v1/schema/``
- ``altair/vega/v3/schema/``
- ``altair/vega/v2/schema/``

All the files within these directories are created automatically by running
the following script from the root of the repository:

```bash
$ python tools/generate_schema_wrapper.py
```

Running this script requires Python 3.6 or newer, though it generates package
code that is compatible with Python 2.7 and 3.5+.

This script does a couple things:

- downloads the appropriate schema files from the specified vega and vega-lite
  release versions & copies the JSON file to the appropriate ``schema``
  directory
- generates basic low-level schemapi wrappers from the definitions within
  the schema: this is put in the ``schema/core.py`` file
- generates a second layer of higher level wrappers for some vega-lite
  functionality; this is put in ``schema/channels.py`` and ``schema/mixins.py``

The script output is designed to be deterministic; if vega/vega-lite versions
are not changed, then running the script should overwrite the schema wrappers
with identical copies.

## Updating the Vega & Vega-Lite versions

The vega & vega-lite versions for the Python code can be updated by manually
changing the ``SCHEMA_VERSION`` definition within
``tools/generate_schema_wrapper.py``, and then re-running the script.

This will update all of the automatically-generated files in the ``schema``
directory for each version, but please note that it will *not* update other
pieces (for example, the core of the Altair API, including methods and
doc strings within ``altair/vegalite/v2/api.py``.
These additional methods have fairly good test coverage, so running the test
suite should identify any inconsistencies:
```
$ make test
```
Generally, minor version updates (e.g. Vega-Lite 2.3->2.4) have been relatively
painless, maybe requiring the addition of a few chart methods or modification
of some docstrings.
Major version updates (e.g. Vega-Lite 1.X->2.X) have required substantial
rewrites, because the internal structure of the schema changed appreciably.


## Releasing the Package

To cut a new release of Altair, follow the steps outlined in
[RELEASING.md](RELEASING.md).