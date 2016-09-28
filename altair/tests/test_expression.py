import numpy as np
import pandas as pd

from .. import vg, expression


def test_func_invocation():
    for func in expression._exp_funcs:
        expr = getattr(vg, func)(vg.d.blah == 2, "hello", vg.LN2, 5.2)
        funcname = expression.NAME_MAP.get(func, func)
        assert expr.eval() == '{0}((datum.blah==2),"hello",LN2,5.2)'.format(funcname)


def test_const_invocation():
    for const in expression._exp_consts:
        expr = (vg.d.blah + getattr(vg, const)) < 2
        constname = expression.NAME_MAP.get(const, const)
        assert expr.eval() == '((datum.blah+{0})<2)'.format(constname)


def test_datum_dir():
    df = pd.DataFrame({'x': np.arange(5),
                       'y': list('abcde'),
                       'z': [1, 2, 1, 1, 2]})
    vgdf = vg.with_df(df)
    assert set(dir(vgdf.d)) == {'x', 'y', 'z'}
