import pytest
import pkgutil

from ...datasets import connection_ok, URLError
from ... import examples
from ... import *


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
    # Don't compare data here, as the JSON representation is tricky
    example = __import__(modname, fromlist="dummy")
    v = example.v
    vdict = v.to_dict(data=False)

    # test that output matches expected output
    assert vdict == example.expected_output

    # test from_dict methods
    v2 = Layer.from_dict(example.expected_output)
    assert v2.to_dict() == vdict

    # test to_altair methods
    v3 = eval(v.to_altair())
    assert v3.to_dict() == vdict
