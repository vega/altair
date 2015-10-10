import os
import pytest
from .. import api

@pytest.fixture
def spec():
    data = dict(x=[1.0, 2.0, 3.0], y=[4.0, 5.0, 6.0])
    result = api.Viz(data).encode(x='x:Q', y='y:Q').line()
    return result

def test_render(spec):
    api.use_renderer('lightning')
    r = spec.render()
    assert r is not None
