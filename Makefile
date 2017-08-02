all: install

install:
	python setup.py install

test :
	py.test altair --doctest-modules

test-examples :
	python tools/create_example_notebooks.py --execute
	rm -rf notebooks/auto_examples
	python tools/create_example_notebooks.py


generate-examples :
	rm -rf notebooks/auto_examples
	python tools/create_example_notebooks.py


generate-schema :
	rm -rf altair/schema/_interface
	python tools/generate_schema_interface.py


sync-examples :
	python tools/sync_vegalite.py --examples


sync-schema :
	python tools/sync_vegalite.py --schema


sync-datasets :
	python tools/sync_vegalite.py --datasets
