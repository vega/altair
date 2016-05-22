"""
Object for generating Python code calls
"""

class CodeGen(object):
    def __init__(self, name, args=None, kwargs=None, methods=None):
        self.name = name
        self.args = (args or [])
        self.kwargs = (kwargs or {})
        self.methods = (methods or [])

    def to_str(self, tablevel=0, tabsize=4):
        """Return a string representation of the code"""
        def get_str(obj, tablevel=tablevel, tabsize=tabsize):
            if isinstance(obj, CodeGen):
                return obj.to_str(tablevel=tablevel, tabsize=tabsize)
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
        self.name = newname
        return self
