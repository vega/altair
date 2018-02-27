import pytest
import warnings
import json

import numpy as np
import pandas as pd

from .. import parse_shorthand, parse_shorthand_plus_data, update_nested


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check('')

    # Fields alone
    check('foobar', field='foobar')
    check('blah:(fd ', field='blah:(fd ')

    # Fields with type
    check('foobar:quantitative', type='quantitative', field='foobar')
    check('foobar:nominal', type='nominal', field='foobar')
    check('foobar:ordinal', type='ordinal', field='foobar')
    check('foobar:temporal', type='temporal', field='foobar')

    check('foobar:Q', type='quantitative', field='foobar')
    check('foobar:N', type='nominal', field='foobar')
    check('foobar:O', type='ordinal', field='foobar')
    check('foobar:T', type='temporal', field='foobar')

    # Fields with aggregate and/or type
    check('average(foobar)', field='foobar', aggregate='average')
    check('min(foobar):temporal', type='temporal', field='foobar', aggregate='min')
    check('sum(foobar):Q', type='quantitative', field='foobar', aggregate='sum')

    # check that invalid arguments are not split-out
    check('invalid(blah)', field='invalid(blah)')
    check('blah:invalid', field='blah:invalid')
    check('invalid(blah):invalid', field='invalid(blah):invalid')

    # check parsing in presence of strange characters
    check('average(a b:(c\nd):Q', aggregate='average',
          field='a b:(c\nd', type='quantitative')


def test_parse_shorthand_plus_data():
    def check(s, data, **kwargs):
        assert parse_shorthand_plus_data(s, data) == kwargs

    data = pd.DataFrame({'x': [1, 2, 3, 4, 5],
                         'y': ['A', 'B', 'C', 'D', 'E'],
                         'z': pd.date_range('2018-01-01', periods=5, freq='D')})

    check('x', data, field='x', type='quantitative')
    check('y', data, field='y', type='nominal')
    check('z', data, field='z', type='temporal')
    check('count(x)', data, field='x', aggregate='count', type='quantitative')
    check('mean(*)', data, field='*', aggregate='mean')


def test_update_nested():
    original = {'x': {'b': {'foo': 2}, 'c': 4}}
    update = {'x': {'b': {'foo': 5}, 'd': 6}, 'y': 40}

    output = update_nested(original, update, copy=True)
    assert output is not original
    assert output == {'x': {'b': {'foo': 5}, 'c': 4, 'd': 6}, 'y': 40}

    output2 = update_nested(original, update)
    assert output2 is original
    assert output == output2
