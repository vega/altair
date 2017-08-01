import pandas as pd

from ._interface import jstraitlets as jst
from . import _interface as schema

from ..utils import sanitize_dataframe


TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantitative': 'Q',
                'temporal': 'T'}


def construct_shorthand(field=None, aggregate=None, type=None):
    """Construct a shorthand representation.

    See also: parse_shorthand"""
    if field is jst.undefined or field is None:
        return ''

    sh = field

    if aggregate is not jst.undefined and aggregate is not None:
        sh = '{0}({1})'.format(aggregate, sh)

    if type is not jst.undefined and type is not None:
        type = TYPECODE_MAP.get(type, type)
        if type not in TYPECODE_MAP.values():
            raise ValueError('Unrecognized Type: {0}'.format(type))
        sh = '{0}:{1}'.format(sh, type)

    return sh


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


class CodeGen(object):
    """Class to generate Python function & Class calls

    Parameters
    ----------
    name : string
        The name of the function or object
    args : list (optional)
        The arguments passed to the function. Each argument should either be
        a string or a CodeGen object.
    kwargs : dict (optional)
        Keyword arguments passed to the function. Each key should be a string;
        Each value should be either a string or CodeGen object.
    methods : list (optional)
        Object methods. Each should be a string or a CodeGen object

    Examples
    --------
    >>> method = CodeGen('bar', ['x', 'y'])
    >>> Foo = CodeGen('Foo', args=[4, 5], methods=[method])
    >>> print(str(Foo))
    Foo(4, 5).bar(x, y)

    >>> code = CodeGen('MyObject', kwargs={'f':Foo, 'flag':True})
    >>> print(str(code))
    MyObject(
        f=Foo(4, 5).bar(x, y),
        flag=True,
    )
    """
    def __init__(self, name, args=None, kwargs=None, methods=None):
        self.name = name
        self.args = (args or [])
        self.kwargs = (kwargs or {})
        self.methods = (methods or [])

    @property
    def num_attributes(self):
        return len(self.args) + len(self.kwargs) + len(self.methods)

    def add_args(self, *args):
        self.args.extend(args)
        return self

    def add_kwargs(self, **kwargs):
        self.kwargs.update(kwargs)
        return self

    def add_methods(self, *methods):
        self.methods.extend(methods)
        return self

    def remove_kwargs(self, *kwds):
        for kwd in kwds:
            self.kwargs.pop(kwd, None)
        return self

    def to_str(self, tablevel=0, tabsize=4):
        """Return a string representation of the code"""
        def get_str(obj, tablevel=tablevel, tabsize=tabsize):
            if isinstance(obj, CodeGen):
                return obj.to_str(tablevel=tablevel, tabsize=tabsize)
            elif isinstance(obj, list):
                return '[{0}]'.format(', '.join(get_str(item,
                                                        tablevel + tabsize)
                                                for item in obj))
            else:
                return str(obj)

        args = [get_str(arg) for arg in self.args]
        kwargs = [((tablevel + tabsize) * ' '
                   + '{0}={1}'.format(k, get_str(v, tablevel + tabsize)))
                  for k, v in sorted(self.kwargs.items())]
        if kwargs:
            kwargs = kwargs + [tablevel * ' ']

        if not kwargs and not args:
            call = '{0}()'.format(self.name)
        elif not kwargs:
            call = '{0}({1})'.format(self.name, ', '.join(args))
        elif not args:
            call = '{0}(\n{1})'.format(self.name, ',\n'.join(kwargs))
        else:
            call = '{0}({1}{2})'.format(self.name, ', '.join(args),
                                        ',\n'.join([''] + kwargs))

        for method in self.methods:
            call += '.{0}'.format(get_str(method))

        return call

    def __str__(self):
        return self.to_str()

    def rename(self, newname):
        """Rename function and return self"""
        self.name = newname
        return self

    def convert_arg_to_method(self, arg, methodname=None, depth=1):
        """Convert an argument (and optionally subarguments) to a method

        Examples
        --------
        >>> encoding = CodeGen('Encoding', kwargs=dict(arg1=1, arg2=2))
        >>> chart = CodeGen('Chart', kwargs=dict(encoding=encoding))
        >>> print(str(chart))
        Chart(
            encoding=Encoding(
                arg1=1,
                arg2=2,
            ),
        )
        >>> chart.convert_arg_to_method('encoding', 'encode')
        >>> print(str(chart))
        Chart().encode(
            arg1=1,
            arg2=2,
        )
        """
        if methodname is None:
            methodname = arg

        def submethods(obj, name, depth):
            """Generate methods, and submethods if depth > 1"""
            if depth > 1:
                # if we're going deeper than one method, then cycle through all
                # arguments and recursively call this function if they are a
                # code object
                for subname, subobj in list(obj.kwargs.items()):
                    if isinstance(subobj, CodeGen):
                        obj.kwargs.pop(subname)
                        subname = '{0}_{1}'.format(name, subname)
                        for method in submethods(subobj, subname, depth - 1):
                            yield method
            if obj.num_attributes > 0:
                # if there are still attributes in the object, yield the
                # top-level method.
                yield obj.rename(name)

        code_obj = self.kwargs.pop(arg, CodeGen(''))
        self.add_methods(*submethods(code_obj, methodname, depth))
