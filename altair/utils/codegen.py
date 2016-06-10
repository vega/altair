"""
Object for generating Python code calls
"""

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
