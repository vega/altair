all: install

install:
	python setup.py install

test :
	py.test altair
