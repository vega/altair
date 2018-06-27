import pandas as pd

import altair as alt
from .. import parse_shorthand, update_nested


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

    # special case: count doesn't need an argument
    check('count()', aggregate='count', type='quantitative')
    check('count():O', aggregate='count', type='ordinal')

    # time units:
    check('month(x)', field='x', timeUnit='month', type='temporal')
    check('year(foo):O', field='foo', timeUnit='year', type='ordinal')
    check('date(date):quantitative',
          field='date', timeUnit='date', type='quantitative')
    check('yearmonthdate(field)', field='field', timeUnit='yearmonthdate', type='temporal')


def test_parse_shorthand_with_data():
    def check(s, data, **kwargs):
        assert parse_shorthand(s, data) == kwargs

    data = pd.DataFrame({'x': [1, 2, 3, 4, 5],
                         'y': ['A', 'B', 'C', 'D', 'E'],
                         'z': pd.date_range('2018-01-01', periods=5, freq='D'),
                         't': pd.date_range('2018-01-01', periods=5, freq='D').tz_localize('UTC')})

    check('x', data, field='x', type='quantitative')
    check('y', data, field='y', type='nominal')
    check('z', data, field='z', type='temporal')
    check('t', data, field='t', type='temporal')
    check('count(x)', data, field='x', aggregate='count', type='quantitative')
    check('count()', data, aggregate='count', type='quantitative')
    check('month(z)', data, timeUnit='month', field='z', type='temporal')
    check('month(t)', data, timeUnit='month', field='t', type='temporal')


def test_parse_shorthand_all_aggregates():
    aggregates = alt.Root._schema['definitions']['AggregateOp']['enum']
    for aggregate in aggregates:
        shorthand = "{aggregate}(field):Q".format(aggregate=aggregate)
        assert parse_shorthand(shorthand) == {'aggregate': aggregate,
                                              'field': 'field',
                                              'type': 'quantitative'}


def test_parse_shorthand_all_timeunits():
    timeUnits = []
    for loc in ['Local', 'Utc']:
        for typ in ['Single', 'Multi']:
            defn = loc + typ + 'TimeUnit'
            timeUnits.extend(alt.Root._schema['definitions'][defn]['enum'])
    for timeUnit in timeUnits:
        shorthand = "{timeUnit}(field):Q".format(timeUnit=timeUnit)
        assert parse_shorthand(shorthand) == {'timeUnit': timeUnit,
                                              'field': 'field',
                                              'type': 'quantitative'}


def test_parse_shorthand_all_window_ops():
    window_ops = alt.Root._schema['definitions']['WindowOnlyOp']['enum']
    aggregates = alt.Root._schema['definitions']['AggregateOp']['enum']
    for op in (window_ops + aggregates):
        shorthand = "{op}(field)".format(op=op)
        dct = parse_shorthand(shorthand,
                              parse_aggregates=False,
                              parse_window_ops=True,
                              parse_timeunits=False,
                              parse_types=False)
        assert dct == {'field': 'field', 'op': op}


def test_update_nested():
    original = {'x': {'b': {'foo': 2}, 'c': 4}}
    update = {'x': {'b': {'foo': 5}, 'd': 6}, 'y': 40}

    output = update_nested(original, update, copy=True)
    assert output is not original
    assert output == {'x': {'b': {'foo': 5}, 'c': 4, 'd': 6}, 'y': 40}

    output2 = update_nested(original, update)
    assert output2 is original
    assert output == output2
