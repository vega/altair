from altair.vegalite import v2 as alt


def test_all_aggregates():
    for aggregate in dir(alt.aggregates):
        if not aggregate.startswith('agg_'):
            continue
        aggfunc = getattr(alt, aggregate)
        print(aggregate)
        name = aggregate.split('_', 1)[1]

        assert aggfunc('foo') == {'field': 'foo',
                                  'aggregate': name,
                                  'type': 'quantitative'}
        assert aggfunc('foo', 'O') == {'field': 'foo',
                                       'aggregate': name,
                                       'type': 'ordinal'}


def test_count_aggregate():
    assert alt.agg_count() == {'aggregate': 'count', 'type': 'quantitative'}
