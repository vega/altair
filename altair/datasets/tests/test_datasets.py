import pytest

from altair import list_datasets, load_dataset



def test_data_by_url():
    for name in list_datasets():
        url = load_dataset(name, url_only=True)
        assert url.startswith('https://')

    bad_dataset = 'blahblahblah'
    with pytest.raises(ValueError) as excinfo:
        load_dataset(bad_dataset)
    assert 'No such dataset {0}'.format(bad_dataset) in str(excinfo.value)
