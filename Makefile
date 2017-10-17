all: install

install:
	python setup.py install

test :
	py.test altair --doctest-modules

generate-schema :
	rm -rf altair/schema/_interface
	python tools/generate_schema_interface.py


sync-examples :
	python tools/sync_vegalite_examples.py


sync-schema :
	python tools/sync_vegalite_schema.py


sync-datasets :
	python tools/sync_vegalite_datasets.py
