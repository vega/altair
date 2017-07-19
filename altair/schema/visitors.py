from ._interface import jstraitlets as jst
from . import _interface as schema


class ToDict(jst.ToDict):
    def _visit_with_data(self, obj, data=True):
        D = self.visit_JSONHasTraits(obj)
        if data:
            if isinstance(obj.data, schema.Data):
                D['data'] = self.visit(obj.data)
            elif isinstance(obj.data, pd.DataFrame):
                values = sanitize_dataframe(obj.data).to_dict(orient='records')
                D['data'] = self.visit(schema.Data(values=values))
        else:
            D.pop('data', None)
        return D

    visit_Chart = _visit_with_data
    visit_LayeredChart = _visit_with_data
    visit_FacetedChart = _visit_with_data


class FromDict(jst.FromDict):
    def clsvisit_Data(self, trait, dct, *args, **kwargs):
        dct = dct.copy()
        values = dct.pop('values', jst.undefined)
        obj = self.clsvisit_JSONHasTraits(trait, dct, *args, **kwargs)
        obj.values = values
        return obj

    def _clsvisit_with_data(self, cls, dct, *args, **kwargs):
        # Remove data first and handle it specially later
        if 'data' in dct:
            dct = dct.copy()
            data = self.clsvisit(schema.Data, dct.pop('data'))
            obj = self.clsvisit_JSONHasTraits(cls, dct)
            obj.data = data
        else:
            obj = self.clsvisit_JSONHasTraits(cls, dct)
        return obj

    clsvisit_Chart = _clsvisit_with_data
    clsvisit_LayeredChart = _clsvisit_with_data
    clsvisit_FacetedChart = _clsvisit_with_data
