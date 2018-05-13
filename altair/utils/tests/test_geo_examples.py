import io
import json
import os
from datetime import datetime

import pytest
import pkgutil
import pandas as pd
import vega_datasets as vds



from altair.utils.execeval import eval_block
from altair.vegalite.v2 import examples



def iter_example_filenames():
    for importer, modname, ispkg in pkgutil.iter_modules(examples.__path__):
        if ispkg or modname.startswith('_'):
            continue
        yield modname + '.py'

class StubGeoDataFrame(pd.DataFrame):
    """Partially emulates GeoDataFrame with fake geometry."""
    used_count = 0
    
    @staticmethod
    def is_used():
        res = StubGeoDataFrame.used_count>0
        StubGeoDataFrame.used_count = 0
        return res
    @property
    def __geo_interface__(self):
        return {
                "type": "FeatureCollection",
                "features":[{"type": "Feature",
                             "geometry": {"type": "Point","coordinates": [125.6, 10.1]},
                             "properties":r } for r in self.to_dict('rows')]
        }
    def __init__(self,*args, **kwargs):
        StubGeoDataFrame.used_count += 1
        super().__init__(*args, **kwargs)
   
    def copy(self, deep=True):
        data = self._data
        if deep:
            data = data.copy()
        return StubGeoDataFrame(data).__finalize__(self)
    def melt(self,*args, **kwargs):
        return StubGeoDataFrame(super().melt(*args, **kwargs))


class DatasetHook:
    """Wraps StubGeoDataFrame over DataFrame in vega_datasets """
    def __init__(self,dataset,datafarme_type):
        self.dataset = dataset
        self.datafarme_type = datafarme_type
    def __call__(self, **kwargs):
        res = self.dataset(**kwargs)
        return StubGeoDataFrame(res) if isinstance (res,self.datafarme_type) else res
    def __getattr__(self, param):
        return self.dataset.__dict__[param]

class DataLoaderHook(vds.DataLoader):
    """Wraps vega_datasets.DataLoader and returns DatasetHook"""
    def __init__(self,datafarme_type):
        self.datafarme_type = datafarme_type

    def __getattr__(self, dataset_name):
        return DatasetHook(super().__getattr__(dataset_name),self.datafarme_type)



def wrap(old,wraper):
    """Wraps old function with wraper"""
    def wrapped(*args, **kwargs):
        return wraper(old(*args, **kwargs))
    return wrapped

class Hacker:
    """Ugly hacker temporary replaces name definition in module. """
    def __init__ (self, module, objects):
        self.new = objects
        self.old = {name: module.__dict__[name] 
                        for name in module.__dict__.keys() & objects.keys()}
        self.module = module
 
    def hack(self):
        self.module.__dict__.update(self.new)
        return self

    def clear(self):
        self.module.__dict__.update(self.old)
        return self

    def __del__(self):
        self.clear()

class Reporter(object):
    def __init__(self,filepath,filename,item):
        self._file = os.path.join(filepath,filename)
        self._item = item

    def __getitem__(self, key):
        if os.path.exists(self._file):
            with open(self._file,'r') as f:
                report = json.load(f)
            return report.get(self._item,{})[key]
        else:
            return None

    def __setitem__(self, key, value):
        report = {self._item:{key:value}}

        if os.path.exists(self._file):
            with open(self._file,'r') as f:
                report = json.load(f)
            item = report.get(self._item,{})
            item[key] = value
            report[self._item] = item

        report['timestamp'] = str(datetime.now())

        with open(self._file,'w') as f:
                json.dump(report,f)


def get_image_file(chart):
    out = io.BytesIO()
    try:
        chart.save(out, format='png')
    except ValueError as err:
        if str(err).startswith('Internet connection'):
            pytest.skip("web connection required for png/svg export")
        else:
            raise
    out.seek(0)
    return out


@pytest.mark.parametrize('filename', iter_example_filenames())
def test_geopandas_examples(filename, report_path=None):
    """GeoDataFrame should result the same image as DataFrame.
    So test compares results of from collection examples 
    with them self but on GeoDataFrame."""
         
    source = pkgutil.get_data(examples.__name__, filename)
    filename = os.path.splitext(filename)[0]
    report = Reporter(report_path, 'report.json',filename) if report_path else None
    
    if report:
        report['result'] = 'fail'

    vds_hack = Hacker(vds, {'data':DataLoaderHook(pd.DataFrame),
                                'DataLoader':DataLoaderHook,
                               }
                        )
    pd_hack = Hacker(pd, {'DataFrame':StubGeoDataFrame,
                             'merge':wrap(pd.merge,StubGeoDataFrame),
                             'melt':wrap(pd.melt,StubGeoDataFrame)
                             }
                        )
  
    try:
        img = {}
      
        for pref in ['gpd','pd']:
            if pref=='gpd':
                vds_hack.hack()
                pd_hack.hack()
            
            StubGeoDataFrame.is_used()

            chart = eval_block(source)
            if chart is None:
                raise ValueError("Example file should define chart in its final "
                            "statement.")
            if not StubGeoDataFrame.is_used() and (pref=='gpd'):
                if report:
                    report['result'] = 'no_pandas'
                return #save test time

            chart.to_dict() 
            pytest.importorskip('selenium')
            if report:
                report[pref+'_vl'] = filename+'_'+pref+'.vl.json'
                chart.save(os.path.join(report_path,report[pref+'_vl']))
            
            img[pref] =  get_image_file(chart)
            if report:
                report[pref+'_png'] = filename+'_'+pref+'.png'
                with open(os.path.join(report_path,report[pref+'_png']),'wb') as f:
                        f.write(img[pref].read())
                        img[pref].seek(0)
            vds_hack.clear()
            pd_hack.clear()
        
        same_img = img['gpd'].read() == img['pd'].read()
        if report:
            report['result'] = ['different','identical'][same_img]
        
        assert same_img
        
    finally:
        vds_hack.clear()
        pd_hack.clear()
  