from altair.utils import parse_shorthand


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check('', type=None)
    check('foobar', type=None, name='foobar')
    check('foobar:nominal', type='N', name='foobar')
    check('foobar:O', type='O', name='foobar')
    check('avg(foobar)', type=None, name='foobar', aggregate='avg')
    check('sum(foobar):Q', type='Q', name='foobar', aggregate='sum')
