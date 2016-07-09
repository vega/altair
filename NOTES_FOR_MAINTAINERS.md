# Notes for Maintainers

Here are a few notes on maintaining & updating altair. Mainly, this is a
collection of notes on the scripts found in the ``tools`` directory, which
help automate the dependency between Altair and Vega-Lite.

Note that everything below (syncing, generating, and testing) can be performed
in a single ``make`` command in altair's root directory.

## Syncing the Schema
The core of the altair codebase is generated automatically by parsing the
Vega-Lite JSON schema. This schema is found at altair/schema/vega-lite-schema.json
This can be updated by manually copying the relevant file from the
[vega-lite repository](http://github.com/vega/vega-lite), but the script
``tools/sync_vegalite.py`` has the ability to take care of this automatically.

For example, to sync version 1.0.12 of the schema, you can run
```
$ python tools/sync_vegalite.py --schema -t v1.0.12
```
where ``v1.0.12`` is the git-tag name for the desired version within the
vega-lite repository.
The default version is hard-coded in ``sync_vegalite.py``,
and when the dependency is updated this default should be changed.
To use the default version, it is sufficient to run
```
$ make sync-schema
```
Note that ``sync_vegalite.py`` requires the [git-python](http://gitpython.readthedocs.io/)
package, which can be installed with
```
$ pip install gitpython
```

### Schema Wrappers
Once the correct schema is in place, the Python wrappers for the schema are
auto-generated using the script ``tools/generate_schema_interface.py``.
This script reads the vega-lite schema, creates basic traitlets wrappers for
all the definitions within it, and also generates some higher-level wrappers.
These are stored in ``altair/schema/_interface`` and ``altair/schema/_wrappers``.
These can be updated by running
```
$ rm -r altair/schema/_interface altair/schema/_wrappers
$ python tools/generate_schema_interface.py
```
The ``rm`` command makes sure no older files hang around if the schema is updated.
For simplicity, this command is built into the makefile:
```
$ make generate-schema
```
For minor updates of the schema, this should be all that is required to update
the dependencies; if the schema update includes more substantial changes, some
of the manual wrappers might have to be updated as well.

Note that the schema generation makes use of Jinja templates, which require
the ``jinja2`` package:
```
$ conda install jinja2
```

## Datasets
The ``altair.load_dataset`` function gives one-line access to all the example
datasets provided by Vega-Lite. These datasets and their descriptions are
listed in ``altair/datasets/datasets.json``. When the Vega-Lite datasets are
updated, this JSON file needs to be updated as well. This can be done using
the information in the [Vega-Lite datasets](https://github.com/vega/vega-datasets.git)
repository. A script to do this automatically is in ``tools/sync_vegalite.py``.
For example, to sync version 1.5.0 of the vega datasets, use
```
$ python tools/sync_vegalite.py --datasets -t v1.5.0
```
Alternatively, to sync the current default version, use
```
$ make sync_datasets
```
As with the schema syncing, this requires the ``git-python`` package (see above).

## Examples
For convenience, Altair includes all the visualization examples from the
Vega-Lite repository. These are stored in ``altair/examples/json/``.
As with the Schema and Datasets, these can be synced using
``tools/sync_vegalite.py``. For example, to sync examples from version 1.0.12,
use
```
$ python tools/sync_vegalite.py --examples -t v1.0.12
```
Alternatively, the default version can be synced using
```
$ make sync-examples
```

### Automatic Altair Examples
Because Altair has the ability to round-trip from Vega-Lite JSON specifications
to Altair specifications and back, we built a script to automatically create
example Jupyter notebooks from the plot examples in Vega-Lite, which are stored
in ``notebooks/auto_examples/``. To generate the
examples from the current set of JSON files in ``altair/examples``, you can run
```
$ python tools/create_example_notebooks.py
```
to optionally execute all the notebooks (and display any exceptions due to
running the code) use
```
$ python tools/create_example_notebooks.py --execute
```
Be warned, though, that this auto-execution takes several minutes!

Avoid committing the executed notebooks to the github repository, though, as
they are much larger than the raw notebooks, and due to Javascript security
concerns, generated plots will not appear on github or nbviewer which negates
any advantage of committing executed notebooks.
