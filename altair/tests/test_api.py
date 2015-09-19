from altair import api

def test_contains():
    d = api.Data()
    assert d.formatType=='json'
    assert 'formatType' in d
    assert d.url==''
    assert 'url' not in d
    assert d.data==[]
    assert 'data' not in d