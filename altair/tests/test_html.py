import os
import tempfile
import shutil
import pytest
from .. import api, spec, html

@pytest.fixture
def spec():
    data = dict(x=[1, 2, 3], y=[4, 5, 6])
    result = api.Viz(data).encode(x='x:Q', y='y:Q').line()
    return result

def test_render(spec):
    r = html.render(spec)
    assert r is not None

def test_save(spec, tmpdir):
    fname = tmpdir.join('test.html').dirname
    html.save(spec, fname)
    assert os.path.exists(fname)

def test_save_rename(spec, tmpdir):
    fname = tmpdir.join('test.html').dirname
    html.save(spec, fname)
    assert(os.path.exists(fname + '.html'))

def test_save_overwrite(spec, tmpdir):
    fname = tmpdir.join('test.html').dirname
    html.save(spec, fname)
    html.save(spec, fname, overwrite=True)
    assert(os.path.exists(fname))

def test_save_overwrite_error(spec, tmpdir):
    fname = tmpdir.join('test.html').dirname
    with pytest.raises(ValueError):
        html.save(spec, fname)
        html.save(spec, fname, overwrite=False)