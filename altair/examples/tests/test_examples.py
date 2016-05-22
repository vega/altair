import os
import pkgutil
import json

import pytest

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


def iter_json_examples():
    json_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            '..', 'json'))
    for json_file in os.listdir(json_dir):
        yield os.path.join(json_dir, json_file)


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


@pytest.mark.skipif(not connection_ok(), reason='No Internet Connection')
@pytest.mark.parametrize('json_path', iter_json_examples())
def test_json_examples_round_trip(json_path):
    """
    Test that Altair correctly round-trips JSON with to_dict() and to_altair()
    """
    with open(json_path) as f:
        json_dict = json.load(f)

    v = Layer.from_dict(json_dict)
    v_dict = v.to_dict()
    assert v_dict == json_dict

    v2 = eval(v.to_altair())
    assert v_dict == v2.to_dict()
