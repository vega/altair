import pytest
import jsonschema

import altair.vegalite.v3 as alt

from contextlib import contextmanager


@contextmanager
def not_raises(ExpectedException):
    try:
        yield

    except ExpectedException as error:
        raise AssertionError(f"Raised exception {error} when it should not!")

    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")

def geom_obj(geom):
    class Geom(object):
        pass
    geom_obj = Geom()
    setattr(geom_obj, '__geo_interface__', geom)
    return geom_obj

# correct translation of Polygon geometry to Feature type
def test_geo_interface_polygon_feature():
    geom = {
        "coordinates": [[
            (0, 0), 
            (0, 2), 
            (2, 2), 
            (2, 0), 
            (0, 0)
        ]],
        "type": "Polygon"
    }
    feat = geom_obj(geom)
    
    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()
    
    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key]['type'] == 'Feature'

# removal of empty `properties` key
def test_geo_interface_removal_empty_properties():
    geom = {
        "geometry": {
            "coordinates": [[
                [6.90, 53.48],
                [5.98, 51.85],
                [6.07, 53.51],
                [6.90, 53.48]
            ]], 
            "type": "Polygon"
        }, 
        "id": None, 
        "properties": {}, 
        "type": "Feature"
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()
    
    ds_key = list(chart['datasets'].keys())[0]
    with pytest.raises(KeyError):
        chart['datasets'][ds_key]['properties']

# correct registration of foreign member (unnest items in `properties`)
def test_geo_interface_register_foreign_member():
    geom = {
        "geometry": {
            "coordinates": [[
                [6.90, 53.48],
                [5.98, 51.85],
                [6.07, 53.51],
                [6.90, 53.48]
            ]], 
            "type": "Polygon"
        }, 
        "id": None, 
        "properties": {"foo": "bah"}, 
        "type": "Feature"
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()

    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key]['foo'] == 'bah'

# correct serializing of arrays and nested tuples
def test_geo_interface_serializing_arrays_tuples():
    import array as arr
    geom = {
        "bbox": arr.array('d', [1, 2, 3, 4]),    
        "geometry": {
            "coordinates": [tuple((
                tuple((6.90, 53.48)),
                tuple((5.98, 51.85)),
                tuple((6.07, 53.51)),
                tuple((6.90, 53.48))
            ))], 
            "type": "Polygon"
        }, 
        "id": 27, 
        "properties": {}, 
        "type": "Feature"
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()

    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key]['bbox'] == [1.0, 2.0, 3.0, 4.0]
    assert chart['datasets'][ds_key]['geometry']['coordinates'][0][0] == [6.9, 53.48]

# keep reserved or existing members within properties
def test_geo_interface_reserved_members():
    geom = {
        "geometry": {
            "coordinates": [[
                [6.90, 53.48],
                [5.98, 51.85],
                [6.07, 53.51],
                [6.90, 53.48]
            ]], 
            "type": "Polygon"
        }, 
        "id": 27, 
        "properties": {"type": "foo"}, 
        "type": "Feature"
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()

    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key]['type'] == 'Feature'
    assert chart['datasets'][ds_key]['properties']['type'] == 'foo'

# an empty FeatureCollection is valid
def test_geo_interface_empty_feature_collection():
    geom = {
        "type": "FeatureCollection",
        "features": []
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()

    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key] == []

# Features in a FeatureCollection shall not overwrite existing or reserved members
def test_geo_interface_feature_collection():
    geom = {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "coordinates": [[
                        [6.90, 53.48],
                        [5.98, 51.85],
                        [6.07, 53.51],
                        [6.90, 53.48]
                    ]], 
                    "type": "Polygon"
                }, 
                "id": 27, 
                "properties": {
                    "type": "foo", 
                    "id": 1, 
                    "geometry": 1
                }, 
                "type": "Feature"
            },    
            {
                "geometry": {
                    "coordinates": [[
                        [8.90, 53.48],
                        [7.98, 51.85],
                        [8.07, 53.51],
                        [8.90, 53.48]
                    ]],
                    "type": "Polygon"
                }, 
                "id": 28, 
                "properties": {
                    "type": "foo", 
                    "id": 2, 
                    "geometry": 1
                }, 
                "type": "Feature"
            },
              
        ]
    }
    feat = geom_obj(geom)

    with not_raises(jsonschema.ValidationError):
        chart = alt.Chart(feat).mark_geoshape().to_dict()

    ds_key = list(chart['datasets'].keys())[0]
    assert chart['datasets'][ds_key][0]['id'] == 27
    assert chart['datasets'][ds_key][1]['id'] == 28
    assert 'coordinates' in chart['datasets'][ds_key][0]['geometry']
    assert 'coordinates' in chart['datasets'][ds_key][1]['geometry'] 
    assert chart['datasets'][ds_key][0]['type'] == 'Feature'
    assert chart['datasets'][ds_key][1]['type'] == 'Feature' 