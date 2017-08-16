import os

import pytest

from ..examples import iter_examples, load_example, iter_examples_with_metadata
from .. import *


def remove_empty_fields(spec):
    """Remove empty entries from the spec"""
    return {k:v for k, v in spec.items() if v}


@pytest.mark.parametrize('example', iter_examples())
def test_json_examples_round_trip(example):
    """
    Test that Altair correctly round-trips JSON with to_dict() and to_python()
    """
    filename, json_dict = example

    v = Chart.from_dict(json_dict)
    v_dict = v.to_dict()
    if '$schema' not in json_dict:
        v_dict.pop('$schema')
    assert v_dict == json_dict

    # code generation discards empty function calls, and so we
    # filter these out before comparison
    v2 = eval(v.to_python())
    v2_dict = v2.to_dict()
    if '$schema' not in json_dict:
        v2_dict.pop('$schema')
    assert v2_dict == remove_empty_fields(json_dict)


def test_load_example():
    filename, spec = next(iter_examples())
    root, _ = os.path.splitext(filename)

    assert load_example(filename) == spec
    assert load_example(root) == spec


@pytest.mark.parametrize('D', iter_examples_with_metadata())
def test_metadata(D):
    expected_keys = {'spec', 'filename', 'category', 'name', 'title'}
    assert len(expected_keys - set(D.keys())) == 0
    assert 'data' in D['spec']
