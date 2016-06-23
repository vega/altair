import os
import pkgutil
import json

import pytest

from .. import iter_examples
from ... import examples
from ... import *


@pytest.mark.parametrize('example', iter_examples())
def test_json_examples_round_trip(example):
    """
    Test that Altair correctly round-trips JSON with to_dict() and to_altair()
    """
    filename, json_dict = example

    v = load_vegalite_spec(json_dict)
    v_dict = v.to_dict()
    assert v_dict == json_dict

    v2 = eval(v.to_altair())
    assert v_dict == v2.to_dict()
