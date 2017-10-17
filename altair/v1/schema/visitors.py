import traitlets as T
import pandas as pd

from ._interface import jstraitlets as jst
from ._interface import schema

from ..traitlet_utils import construct_shorthand
from ...utils import sanitize_dataframe, CodeGen


class ToDict(jst.ToDict):
    def _visit_with_data(self, obj, data=True, **kwargs):
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


class ToPython(jst.ToPython):
    def visit_list(self, obj, *args, **kwargs):
        return [self.visit(o) for o in obj]
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj._skip_on_export and
                getattr(obj, k, jst.undefined) is not jst.undefined}
        kwds = {k: self.visit(v) for k, v in kwds.items()}
        return CodeGen(obj.__class__.__name__, kwargs=kwds)

    def visit_JSONHasTraits(self, obj, *args, **kwargs):
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj._skip_on_export and
                getattr(obj, k, jst.undefined) is not jst.undefined}
        missing = set(obj._required_traits) - set(kwds)
        if missing:
            raise jst.UndefinedTraitError("Required traits {0} missing"
                                          "".format(missing))
        kwds = {k: self.visit(v) for k, v in kwds.items()}
        return CodeGen(obj.__class__.__name__, kwargs=kwds)

    def _visit_ChannelWrapper(self, obj, *args, **kwargs):
        if obj.shorthand:
            shorthand = obj.shorthand
        else:
            shorthand = construct_shorthand(field=obj.field,
                                            aggregate=obj.aggregate,
                                            type=obj.type)
        code = self.visit_JSONHasTraits(obj)
        if shorthand:
            code.add_args(repr(shorthand))
        code.remove_kwargs('field', 'aggregate', 'type')

        do_shorten = (shorthand
                      and kwargs.get('shorten', False)
                      and len(code.args) == 1
                      and not (code.kwargs or code.methods))
        if do_shorten:
            return repr(shorthand)
        else:
            return code

    visit_ChannelWithLegend = _visit_ChannelWrapper
    visit_Field = _visit_ChannelWrapper
    visit_OrderChannel = _visit_ChannelWrapper
    visit_PositionChannel = _visit_ChannelWrapper

    def visit_Encoding(self, obj, *args, **kwargs):
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj._skip_on_export
                and getattr(obj, k, jst.undefined) is not jst.undefined}
        kwds = {k: self.visit(v, shorten=True) for k, v in kwds.items()}
        return CodeGen(obj.__class__.__name__, kwargs=kwds)

    def _visit_with_data(self, obj, data=None, *args, **kwargs):
        code = self.visit_JSONHasTraits(obj)

        # Add data as a top-level argument
        if data is not None:
            # data as a user-speficied name
            code.add_args(data)
        elif isinstance(obj.data, schema.Data):
            # data as a Data trait: return raw URL if possible
            url_only = ('url' in obj.data and
                        'values' not in obj.data and
                        'format' not in obj.data)
            if url_only:
                code.add_args("'{0}'".format(obj.data.url))
            else:
                code.add_args(self.visit(obj.data))
        elif isinstance(obj.data, pd.DataFrame):
            # data as a dataframe; this gets too long so we leave it out
            warnings.warn("Skipping dataframe definition in altair code")

        return code

    def visit_Chart(self, obj, data=None, *args, **kwargs):
        code = self._visit_with_data(obj, data, *args, **kwargs)

        # enable Chart().mark_point(**kwargs)
        mark = code.kwargs.pop('mark', None)
        if mark:
            config = code.kwargs.get('config', CodeGen(''))
            markconfig = config.kwargs.pop('mark', CodeGen(''))
            code.add_methods(markconfig.rename('mark_{0}'.format(obj.mark)))

        # enable Chart().encode(**kwargs)
        code.convert_arg_to_method('encoding', 'encode', depth=1)

        # enable Chart().transform_data(**kwargs)
        code.convert_arg_to_method('transform', 'transform_data', depth=1)

        # enable Chart().configure(**kwargs)
        #                configure_<arg>(**kwargs)
        #                configure_facet_<arg>(**kwargs)
        code.convert_arg_to_method('config', 'configure', depth=3)

        return code

    visit_LayeredChart = _visit_with_data
    visit_FacetedChart = _visit_with_data
