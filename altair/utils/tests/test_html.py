import json
from ..html import to_html


def test_to_html():
    json_dict = dict(A=1, B={'C':2, 'D':3})
    title = 'My Awesome Title'

    # Smoke-test for the basic template
    html = to_html(json_dict, title=title)
    assert '<title>{0}</title>'.format(title) in html

    # Test a custom template
    custom_template = "{spec}<@>{title}"
    html = to_html(json_dict, title=title, template=custom_template)
    spec, embedded_title = html.split('<@>')
    assert json.loads(spec) == json_dict
    assert embedded_title == title
