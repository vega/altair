all: install

install:
	python setup.py install

test :
	python -m pytest --pyargs --doctest-modules altair

test-coverage:
	python -m pytest --pyargs --doctest-modules --cov=altair --cov-report term altair

test-coverage-html:
	python -m pytest --pyargs --doctest-modules --cov=altair --cov-report html altair
