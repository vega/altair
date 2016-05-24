import pandas as pd

from .schema import Data
from .utils import sanitize_dataframe


class Visitor(object):
    """Class implementing the external visitor pattern"""
    def visit(self, obj, *args, **kwargs):
        for cls in obj.__class__.__mro__:
            method = getattr(self, 'visit_' + cls.__name__, None)
            if method: break
        else:
            method = self.generic_visit
        return method(obj, *args, **kwargs)

    def generic_visit(self, obj, *args, **kwargs):
        raise NotImplementedError()


class DictOutputVisitor(Visitor):
    def visit_BaseObject(self, obj, *args, **kwargs):
        D = {}
        for k in obj.traits():
            if k in obj and k not in obj.skip:
                v = getattr(obj, k)
                if v is not None:
                    D[k] = self.visit(v)
        return D

    def visit_Layer(self, obj, data, *args, **kwargs):
        D = self.visit_BaseObject(obj)
        if data:
            if isinstance(obj.data, Data):
                D['data'] = self.visit(obj.data)
            elif isinstance(obj.data, pd.DataFrame):
                values = sanitize_dataframe(obj.data).to_dict(orient='records')
                D['data'] = self.visit(Data(values=values))
        else:
            D.pop('data', None)
        return D

    def visit_list(self, obj, *args, **kwargs):
        return [self.visit(o) for o in obj]

    def generic_visit(self, obj, *args, **kwargs):
        return obj
