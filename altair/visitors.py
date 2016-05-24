import pandas as pd
import traitlets as T

from . import schema
from .codegen import CodeGen
from .utils import sanitize_dataframe, construct_shorthand


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
        return method(obj, *args, **kwargs)


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

    def visit_Layer(self, obj, data):
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


class ToCode(Visitor):
    """Crawl object structure to output code"""
    def generic_visit(self, obj, *args, **kwargs):
        return repr(obj)

    def visit_list(self, obj, *args, **kwargs):
        return [self.visit(o) for o in obj]

    def visit_BaseObject(self, obj, ignore_kwds=None, extra_args=None,
                         extra_kwds=None, methods=None):
        kwds = {k: getattr(obj, k) for k in obj.traits()
                if k not in obj.skip
                and k not in (ignore_kwds or [])
                and k in obj}  # k in obj also checks whether k is defined
        kwds.update(extra_kwds or {})
        kwds = {k: self.visit(v) for k, v in kwds.items()}

        return CodeGen(obj.__class__.__name__,
                       args=extra_args or [],
                       kwargs=kwds,
                       methods=methods)

    def visit__ChannelMixin(self, obj, shorten=True, ignore_kwds=None,
                            extra_args=None, extra_kwds=None, methods=None):
        shorthand = construct_shorthand(field=obj.field,
                                        aggregate=obj.aggregate,
                                        type=obj.type)
        extra_args = [repr(shorthand)] + (extra_args or [])

        ignore_kwds = (ignore_kwds or [])
        ignore_kwds.extend(['field', 'aggregate', 'type'])
        code = self.visit_BaseObject(obj, ignore_kwds=ignore_kwds,
                                     extra_args=extra_args,
                                     extra_kwds=extra_kwds,
                                     methods=methods)

        do_shorten = (shorten and len(code.args) == 1
                      and not (code.kwargs or code.methods))
        if do_shorten:
            return repr(shorthand)
        else:
            return code

    def visit_Layer(self, obj, data=None, ignore_kwds=None,
                    extra_args=None, extra_kwds=None, methods=None):
        extra_args = (extra_args or [])
        ignore_kwds = (ignore_kwds or [])

        if data:
            extra_args.append(data)
        elif isinstance(obj.data, schema.Data):
            url_only = ('url' in obj.data and
                        'values' not in obj.data and
                        'formatType' not in obj.data)
            if url_only:
                extra_args.append("'{0}'".format(obj.data.url))
            else:
                extra_args.append(self.visit(obj.data))
        elif isinstance(obj.data, pd.DataFrame):
            warnings.warn("Skipping dataframe definition in altair code")

        ignore_kwds.extend(['mark', 'encoding', 'transform', 'config'])
        methods = (methods or [])

        if obj.mark:
            methods.append(CodeGen('mark_{0}'.format(obj.mark)))
        if obj.encoding:
            methods.append(self.visit(obj.encoding).rename('encode'))
        if obj.transform:
            methods.append(self.visit(obj.transform).rename('transform_data'))
        if obj.config:
            methods.append(self.visit(obj.config).rename('configure'))

        return self.visit_BaseObject(obj, ignore_kwds=ignore_kwds,
                                     extra_args=extra_args,
                                     extra_kwds=extra_kwds,
                                     methods=methods)


class FromDict(Visitor):
    """Crawl object structure to construct object from a Dictionary"""
    def clsvisit_BaseObject(self, cls, dct):
        try:
            obj = cls()
        except TypeError as err:  # Argument missing
            obj = cls('')

        for prop, val in dct.items():
            if not obj.has_trait(prop):
                raise ValueError("{0} not a valid property in {1}"
                                 "".format(prop, cls))
            trait = obj.traits()[prop]
            obj.set_trait(prop, self.visit(trait, val))
        return obj

    def clsvisit_Layer(self, cls, dct):
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

    def visit_List(self, trait, dct):
        return [self.visit(trait._trait, item) for item in dct]

    def visit_Instance(self, trait, dct):
        if not isinstance(dct, dict):
            return dct
        return self.clsvisit(trait.klass, dct)

    def visit_Union(self, trait, dct):
        if not isinstance(dct, dict):
            return dct
        for subtrait in trait.trait_types:
            try:
                return self.visit(subtrait, dct)
            except T.TraitError:
                pass

    def visit_BaseObject(self, trait, dct):
        if not isinstance(dct, dict):
            return dct
        return generic_visit(self, trait, dct)

    def generic_visit(self, trait, dct):
        if not isinstance(dct, dict):
            return dct
        raise T.TraitError('cannot set {0} to {1}'.format(trait, dct))
