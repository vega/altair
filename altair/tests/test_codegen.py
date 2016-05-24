# TODO: add some tests of CodeGen
from ..codegen import CodeGen


def test_args():
    code = CodeGen('Foo', ['x', 'y', 'z'])
    assert str(code) == 'Foo(x, y, z)'


def test_kwargs():
    code = CodeGen('Bar', kwargs={'a':4, 'b':5, 'c':6})
    assert str(code) == '\n'.join(["Bar(",
                                   "    a=4,",
                                   "    b=5,",
                                   "    c=6,",
                                   ")"])


def test_code_as_arg():
    code = CodeGen('Foo', ['x', 'y', 'z'])
    code2 = CodeGen('Bar', kwargs=dict(foo=code))
    assert str(code2) == '\n'.join(['Bar(',
                                    '    foo=Foo(x, y, z),',
                                    ')'])


def test_methods():
    bar = CodeGen('bar', [1, 2, 3])
    code = CodeGen('Foo', 'x', methods=[bar])
    assert str(code) == 'Foo(x).bar(1, 2, 3)'
