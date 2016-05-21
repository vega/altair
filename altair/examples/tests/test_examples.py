import pytest
import pkgutil

from ...datasets import connection_ok, URLError
from ... import examples


def iter_submodules(package, include_packages=False):
    """Iterate importable submodules of a module"""
    prefix = package.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix):
        if not include_packages and ispkg:
            continue
        yield modname


@pytest.mark.skipif(not connection_ok(), reason='No Internet Connection')
@pytest.mark.parametrize('modname', iter_submodules(examples))
def test_examples_output(modname):
    example = __import__(modname, fromlist="dummy")
    assert example.v.to_dict() == example.expected_output
