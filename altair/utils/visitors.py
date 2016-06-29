import warnings

import pandas as pd
import traitlets as T

from ._py3k_compat import integer_types, string_types
from .. import schema
from .codegen import CodeGen
from . import sanitize_dataframe, construct_shorthand


class Visitor(object):
    """Class implementing the external visitor pattern"""
    def visit(self, obj, *args, **kwargs):
        for cls in obj.__class__.__mro__:
            method = getattr(self, 'visit_' + cls.__name__, None)
            if method:
                break
        else:
            method = self.generic_visit
        return method(obj, *args, **kwargs)

    def clsvisit(self, obj, *args, **kwargs):
        for cls in obj.__mro__:
            method = getattr(self, 'clsvisit_' + cls.__name__, None)
            if method:
                break
        else:
            method = self.generic_clsvisit
        try:
            return method(obj, *args, **kwargs)
        except KeyError:
            print(obj)
            print(args)
            print(kwargs)
            raise


class ToDict(Visitor):
    """Crawl object structure to output dictionary"""
    def generic_visit(self, obj, *args, **kwargs):
        return obj

    def visit_list(self, obj, *args, **kwargs):
            return [self.visit(o) for o in obj]

    def visit_BaseObject(self, obj, *args, **kwargs):
        D = {}
        for k in obj.traits():
            if k in obj and k not in obj.skip:
                v = getattr(obj, k)
                if v is not None:
                    D[k] = self.visit(v)
        return D

    def _visit_with_data(self, obj, data=True):
        D = self.visit_BaseObject(obj)
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


class ToCode(Visitor):
    """Crawl object structure to output code"""
    def generic_visit(self, obj, *args, **kwargs):
        return repr(obj)

    def visit_list(self, obj, *args, **kwargs):
        return [self.visit(o) for o in obj]

    def visit_BaseObject(self, obj, *args, **kwargs):
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj.skip and k in obj}
        kwds = {k: self.visit(v) for k, v in kwds.items()}
        return CodeGen(obj.__class__.__name__, kwargs=kwds)

    def _visit_ChannelWrapper(self, obj, *args, **kwargs):
        if obj.shorthand:
            shorthand = obj.shorthand
        else:
            shorthand = construct_shorthand(field=obj.field,
                                            aggregate=obj.aggregate,
                                            type=obj.type)
        code = self.visit_BaseObject(obj)
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

    def visit_ChannelWithLegend(self, obj, *args, **kwargs):
        return self._visit_ChannelWrapper(obj, *args, **kwargs)

    def visit_Field(self, obj, *args, **kwargs):
        return self._visit_ChannelWrapper(obj, *args, **kwargs)

    def visit_OrderChannel(self, obj, *args, **kwargs):
        return self._visit_ChannelWrapper(obj, *args, **kwargs)

    def visit_PositionChannel(self, obj, *args, **kwargs):
        return self._visit_ChannelWrapper(obj, *args, **kwargs)

    def visit_Encoding(self, obj, *args, **kwargs):
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj.skip and k in obj}
        kwds = {k: self.visit(v, shorten=True) for k, v in kwds.items()}
        return CodeGen(obj.__class__.__name__, kwargs=kwds)

    def _visit_with_data(self, obj, data=None, *args, **kwargs):
        code = self.visit_BaseObject(obj)

        # Add data as a top-level argument
        if data is not None:
            # data as a user-speficied name
            code.add_args(data)
        elif isinstance(obj.data, schema.Data):
            # data as a Data trait: return raw URL if possible
            url_only = ('url' in obj.data and
                        'values' not in obj.data and
                        'formatType' not in obj.data)
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

    def visit_LayeredChart(self, obj, data=None, *args, **kwargs):
        return self._visit_with_data(obj, data, *args, **kwargs)

    def visit_FacetedChart(self, obj, data=None, *args, **kwargs):
        return self._visit_with_data(obj, data, *args, **kwargs)


class FromDict(Visitor):
    """Crawl object structure to construct object from a Dictionary"""
    def clsvisit_BaseObject(self, cls, dct, *args, **kwargs):
        try:
            obj = cls()
        except TypeError as err:  # Argument missing
            obj = cls('')

        for prop, val in dct.items():
            subtrait = obj.traits()[prop]
            obj.set_trait(prop, self.visit(subtrait, val))
        return obj

    def _clsvisit_with_data(self, cls, dct, *args, **kwargs):
        # Remove data first and handle it specially later
        if 'data' in dct:
            dct = dct.copy()
        data = dct.pop('data', None)

        obj = self.clsvisit_BaseObject(cls, dct)

        # data is not a typical trait; do special handling here.
        if data is not None:
            values_only = ('values' in data and
                           'url' not in data and
                           'dataFormat' not in data)
            if values_only:
                obj.data = pd.DataFrame(data['values'])
            else:
                obj.data = schema.Data(**data)
        return obj

    clsvisit_Chart = _clsvisit_with_data
    clsvisit_LayeredChart = _clsvisit_with_data
    clsvisit_FacetedChart = _clsvisit_with_data

    def visit_List(self, trait, dct, *args, **kwargs):
        return [self.visit(trait._trait, item) for item in dct]

    def visit_Instance(self, trait, dct, *args, **kwargs):
        try:
            return self.generic_visit(trait, dct)
        except T.TraitError:
            return self.clsvisit(trait.klass, dct)

    def visit_Union(self, trait, dct, *args, **kwargs):
        try:
            return self.generic_visit(trait, dct)
        except T.TraitError:
            for subtrait in trait.trait_types:
                try:
                    return self.visit(subtrait, dct)
                except T.TraitError:
                    pass
            raise  # no valid trait found

    def generic_visit(self, trait, dct, *args, **kwargs):
        # pass-through simple types
        if isinstance(dct, (integer_types, string_types, bool, float)):
            return dct
        else:
            raise T.TraitError('cannot set {0} to {1}'.format(trait, dct))
