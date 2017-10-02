import pytest
import os
import warnings
import json

import numpy as np
import pandas as pd

from .. import (
    Vega, VegaLite, VEGA_MIME_TYPE, VEGALITE_MIME_TYPE,
    create_vega_mime_bundle, create_vegalite_mime_bundle
)

from ... import Chart

_data = pd.DataFrame({
    'x': np.random.rand(10),
    'y': np.random.rand(10),
    'c': list('abcdefghij')
})

_spec = {
    "encoding": {
        "c": {
            "field": "Origin",
            "type": "nominal"
        },
        "x": {
            "field": "x",
            "type": "quantitative"
        },
        "y": {
            "field": "y",
            "type": "quantitative"
        }
    },
    "mark": "point"
}

def test_create_vegalite_mimebundle():
    bundle = create_vegalite_mime_bundle(_spec, data=_data)
    assert 'text/plain' in bundle
    assert VEGALITE_MIME_TYPE in bundle
    spec = bundle[VEGALITE_MIME_TYPE]
    assert 'data' in spec
    assert 'encoding' in spec
    assert 'mark' in spec
    assert spec['encoding'] == _spec['encoding']

def test_VegaLite():
    vl = VegaLite(_spec, _data)
    assert vl.spec == _spec
    from altair import examples
    filename = os.path.abspath(
        os.path.join(examples.JSON_DIR, 'area.vl.json')
    )
    vl = VegaLite(filename=filename)
    assert vl.spec['mark']=='area'
    assert 'encoding' in vl.spec
    assert vl.data is None
