import pytest
import pandas as pd
import altair.vegalite.v2 as alt

from ..data import  pipe, to_values, to_csv
from .. import parse_shorthand


def _create_geojson():
    return {
                "type": "FeatureCollection",
                "bbox": [
                    -161.30174569731454,
                    -60.39157788643298,
                    172.67580002536624,
                    42.438347020953984
                ],
                "features": [
                    {
                    "type": "Feature",
                    "properties": {"prop": 1},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                        [-69.2980008004234, 23.18780298146116],
                        [-161.30174569731454, -60.39157788643298],
                        [172.67580002536624, 24.151450472748962]
                        ]
                    },
                    "id": "0",
                    "bbox": [
                        -161.30174569731454,
                        -60.39157788643298,
                        172.67580002536624,
                        24.151450472748962
                    ]
                    },
                    {
                    "type": "Feature",
                    "properties": {"prop": 2},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                        [156.03047546751765, 42.438347020953984],
                        [35.46296546950265, -18.185542212943375],
                        [152.53211600051463, 23.471406463455793]
                        ]
                    },
                    "id": "1",
                    "bbox": [
                        35.46296546950265,
                        -18.185542212943375,
                        156.03047546751765,
                        42.438347020953984
                    ]
                    },
                    {
                    "type": "Feature",
                    "properties": {"prop": 3},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                        [-133.98414913936503, 25.39468871174894],
                        [145.04376601680605, 13.058626381790845],
                        [170.30576801294046, 38.67128737163435]
                        ]
                    },
                    "id": "2",
                    "bbox": [
                        -133.98414913936503,
                        13.058626381790845,
                        170.30576801294046,
                        38.67128737163435
                    ]
                    }
                ]
            }

def _create_fake_geo_interface():
    class FakeGeoJSON:
        __geo_interface__=_create_geojson()
    return FakeGeoJSON()

def _create_fake_geodataframe():
    class FakeGeoDataFrame(pd.DataFrame):
        __geo_interface__=_create_geojson()
        def copy(self, deep=True):
            data = self._data
            if deep:
                data = data.copy()
            return FakeGeoDataFrame(data).__finalize__(self)

    return FakeGeoDataFrame({'prop':[1,2,3]})
 
def test_to_values_geo():
    """Test the to_values data transformer."""
    
    data = _create_fake_geodataframe()
    result = pipe(data, to_values)
    assert result['format'] == {'type':'json','property':'features'}
    assert result['values']==data.__geo_interface__

    data = _create_fake_geo_interface()
    result = pipe(data, to_values)
    assert result['format'] == {'type':'json'}
    assert result['values']==data.__geo_interface__

def test_chart_data_geotypes():
    Chart = lambda data,**arg: alt.Chart(data).mark_geoshape().project().encode(**arg)

    # Fake GeoPandas
    data = _create_fake_geodataframe()
    dct = Chart(data,fill='prop').to_dict() 
    assert dct['data']['format'] == {'type':'json','property':'features'}
    assert dct['data']['values'] == data.__geo_interface__

    # Fake GeoInterface
    data = _create_fake_geo_interface()
    dct = Chart(data).to_dict() 
    assert dct['data']['format'] == {'type':'json'}
    assert dct['data']['values'] == data.__geo_interface__

def test_parse_shorthand_with_geodata():
    def check(s, data, **kwargs):
        assert parse_shorthand(s, data) == kwargs

    data = _create_fake_geodataframe()

    check('prop', data, field='properties.prop', type='quantitative',title='prop')
    check('prop:N', data, field='properties.prop', type='nominal',title='prop')
    check('count(prop)', data, field='properties.prop', aggregate='count', type='quantitative',title='prop')
    
    data = _create_fake_geo_interface()

    check('properties.prop:Q', data, field='properties.prop', type='quantitative')
    check('prop', data, field='prop')

def test_to_csv_geo():
    """Test the to_csv raise error with geopandas."""
    
    data = _create_fake_geodataframe()
    with pytest.raises(NotImplementedError):
        pipe(data, to_csv)

def test_geo_pandas(): 
    gpd = pytest.importorskip('geopandas')
    
    data = gpd.GeoDataFrame.from_features(_create_geojson())
    dct = alt.Chart(data).mark_geoshape().project().encode(fill='prop').to_dict()
    
    assert dct['data']['format'] == {'type':'json','property':'features'}
    assert (gpd.GeoDataFrame.from_features(dct['data']['values']) == data).all().all()
    assert dct['encoding'] == {'fill': {'field': 'properties.prop', 'type': 'quantitative','title':'prop'}}

def test_geojson_feature():
    Chart = lambda data,**arg: alt.Chart(alt.geojson_feature(data,'test_prop')
                                        ).mark_geoshape().project().encode(**arg)

    # Fake GeoInterface
    data = _create_fake_geo_interface() 
    dct = Chart(data).to_dict() 

    assert dct['data']['format'] == {'type':'json','property':'test_prop'}
    assert dct['data']['values'] == data.__geo_interface__
    
    # url
    data = "url.json"
    dct = Chart(data).to_dict() 

    assert dct['data']['format'] == {'type':'json','property':'test_prop'}
    assert dct['data']['url'] == data
