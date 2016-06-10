test :
	py.test altair --doctest-modules


generate-examples :
	python tools/create_example_notebooks.py


generate-schema :
	python tools/generate_schema_interface.py


sync-examples :
	python tools/sync_vegalite.py --examples


sync-schema :
	python tools/sync_vegalite.py --schema


sync-datasets :
	python tools/sync_vegalite.py --datasets
