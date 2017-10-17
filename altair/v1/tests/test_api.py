import pytest
import warnings
import json
import tempfile

import numpy as np
import pandas as pd

from .. import *
from .. import schema
from ..schema import jstraitlets as jst
from ..examples import iter_examples
from ...datasets import connection_ok
from ...utils.node import consistent_with_png, consistent_with_svg
from ...utils._py3k_compat import PY2

def make_chart():
    data = pd.DataFrame({'x': range(10),
                         'y': range(10)})
    return Chart(data).mark_point().encode(x='x', y='y')


def test_default_mark():
    """Make sure the default mark is a point."""
    c = Chart()
    assert c.mark=='point'


def test_mark_methods():
    """Make sure the Chart's mark_*() methods all exist"""
    from ..schema import Mark
    assert set(Mark().values) == {method.split('_')[1]
                                  for method in dir(Chart)
                                  if method.startswith('mark_')}


def test_chart_url_input():
    url = 'http://vega.github.io/vega-lite/data/'
    chart1 = Chart(Data(url=url))
    chart2 = Chart(url)

    assert chart1.to_dict() == chart2.to_dict()
    assert chart1.to_python() == chart2.to_python()


def test_chart_to_html():
    chart = Chart().encode(x='blah:Q')
    html = chart.to_html(title='My Chart')
    assert "<title>My Chart</title>" in html

    html = chart.to_html(template="{title}<@>{spec}")
    title, spec = html.split('<@>')
    assert json.loads(spec) == chart.to_dict()
    assert title == "Vega-Lite Chart"


def test_chart_to_json_round_trip():
    chart1 = Chart('data/data.json').mark_point().encode(x='blah:Q')
    chart2 = Chart.from_json(chart1.to_json())
    assert chart1.to_dict() == chart2.to_dict()


@pytest.mark.skipif(not Chart._png_output_available(),
                    reason='command-line tool vl2png is not available')
def test_savechart_png():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        chart.savechart(f.name)
        assert consistent_with_png(f.name)


@pytest.mark.skipif(not Chart._svg_output_available(),
                    reason='command-line tool vl2svg is not available')
def test_savechart_svg():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.svg') as f:
        chart.savechart(f.name)
        assert consistent_with_svg(f.name)


def test_savechart_html():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.html') as f:
        chart.savechart(f.name)
        content = f.read()
        if hasattr(content, 'decode'):
            content = content.decode('utf-8')
        assert content.strip().startswith('<!DOCTYPE html>')


def test_savechart_json():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.json') as f:
        chart.savechart(f.name)
        assert chart.to_dict() == json.load(open(f.name))


def test_encode_update():
    # Test that encode updates rather than overwrites
    chart1 = Chart().encode(x='blah:Q').encode(y='blah:Q')
    chart2 = Chart().encode(x='blah:Q', y='blah:Q')

    assert chart1.to_dict() == chart2.to_dict()


def test_configure_update():
    # Test that configure updates rather than overwrites
    chart1 = Chart().configure(MarkConfig(color='red'))\
                    .configure(background='red')
    chart2 = Chart().configure(MarkConfig(color='red'), background='red')

    assert chart1.to_dict() == chart2.to_dict()


def test_configure_axis_update():
    chart1 = Chart().configure_axis(axisColor='red')\
                    .configure_axis(axisWidth=100)
    chart2 = Chart().configure_axis(axisColor='red',
                                    axisWidth=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_cell_update():
    chart1 = Chart().configure_cell(stroke='red')\
                    .configure_cell(height=100)
    chart2 = Chart().configure_cell(stroke='red',
                                    height=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_legend_update():
    chart1 = Chart().configure_legend(gradientStrokeColor='red')\
                    .configure_legend(gradientHeight=100)
    chart2 = Chart().configure_legend(gradientStrokeColor='red',
                                      gradientHeight=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_mark_update():
    chart1 = Chart().configure_mark(color='red')\
                    .configure_mark(angle=90)
    chart2 = Chart().configure_mark(color='red',
                                    angle=90)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_scale_update():
    chart1 = Chart().configure_scale(bandSize=50)\
                    .configure_scale(round=True)
    chart2 = Chart().configure_scale(bandSize=50,
                                     round=True)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_facet_axis_update():
    chart1 = Chart().configure_facet_axis(axisColor='red')\
                    .configure_facet_axis(axisWidth=100)
    chart2 = Chart().configure_facet_axis(axisColor='red',
                                          axisWidth=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_facet_cell_update():
    chart1 = Chart().configure_facet_cell(stroke='red')\
                    .configure_facet_cell(height=100)
    chart2 = Chart().configure_facet_cell(stroke='red',
                                          height=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_facet_grid_update():
    chart1 = Chart().configure_facet_grid(color='red')\
                    .configure_facet_grid(offset=100)
    chart2 = Chart().configure_facet_grid(color='red',
                                          offset=100)
    assert chart1.to_dict() == chart2.to_dict()


def test_configure_facet_scale_update():
    chart1 = Chart().configure_facet_scale(padding=50)\
                    .configure_facet_scale(round=True)
    chart2 = Chart().configure_facet_scale(padding=50,
                                           round=True)
    assert chart1.to_dict() == chart2.to_dict()


def test_transform_update():
    # Test that transform updates rather than overwrites
    formula = Formula(field='gender', expr='datum.sex == 2 ? "Female":"Male"')
    chart1 = Chart().transform_data(filter='datum.year==2000')\
                    .transform_data(calculate=[formula])

    chart2 = Chart().transform_data(filter='datum.year==2000',
                                    calculate=[formula])

    assert chart1.to_dict() == chart2.to_dict()


def test_Chart_from_dict():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Chart(df).mark_point().encode(x='x', y='y')
    obj2 = Chart.from_dict(obj.to_dict())
    assert obj.to_dict() == obj2.to_dict()


def test_Chart_load_example():
    filename, spec = next(iter_examples())
    chart1 = Chart.from_dict(spec)
    chart2 = Chart.load_example(filename)

    assert chart1.to_dict() == chart2.to_dict()


def test_to_python():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Chart(df).mark_point().encode(x='x', y='y')

    code = obj.to_python(data='df')
    obj2 = eval(code)

    assert obj.to_dict() == obj2.to_dict()


def test_to_python_with_methods():
    from ...utils._py3k_compat import PY2
    if PY2:
        code_in = "Chart('http://vega.github.io').mark_point(color=u'red',)"
    else:
        code_in = "Chart('http://vega.github.io').mark_point(color='red',)"
    code_out = eval(code_in).to_python()
    assert code_in == code_out.replace(' ', '').replace('\n','')


@pytest.mark.skipif(not connection_ok(), reason="No Internet Connection")
def test_to_python_stocks():
    """Test a more complicated spec for conversion to altair"""
    data = load_dataset('stocks')

    chart = Chart(data).mark_line().encode(
        x='date:T',
        y='price:Q'
    ).transform_data(
        filter="datum.symbol==='GOOG'"
    ).configure(
        mark=MarkConfig(color='red')
    )

    code = chart.to_python(data='data')
    chart2 = eval(code)

    assert chart.to_dict() == chart2.to_dict()


@pytest.mark.parametrize('mark', schema.Mark().values)
def test_mark_config(mark):
    markmethod = lambda chart: getattr(chart, 'mark_' + mark)
    kwds = dict(color='red', opacity=0.5)

    chart1 = Chart(config=Config(mark=MarkConfig(**kwds)))
    # chart1.mark_circle()
    markmethod(chart1)()
    chart1.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    chart2 = Chart()
    # chart2.mark_circle(color='red')
    markmethod(chart2)(**kwds)
    chart2.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    chart3 = Chart()
    #chart3.mark_circle().configure_mark(**kwargs)
    markmethod(chart3)().configure_mark(**kwds)
    chart3.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    assert chart1.to_dict() == chart2.to_dict()
    assert chart2.to_dict() == chart3.to_dict()


_config_method_params = [
    {'name': 'axis',
     'class': AxisConfig,
     'kwds': dict(axisWidth=1.0, grid=False)
    },
    {'name': 'cell',
     'class': CellConfig,
     'kwds': dict(clip=False, fillOpacity=0.5)
    },
    {'name': 'legend',
     'class': LegendConfig,
     'kwds': dict(orient=u'foo', shortTimeLabels=True)
    },
    {'name': 'scale',
     'class': ScaleConfig,
     'kwds': dict(pointSizeRange=[1.0, 2.0], round=False)
    },
]

@pytest.mark.parametrize('params', _config_method_params)
def test_config_methods(params):
    kwds = params['kwds']
    klass = params['class']
    name = params['name']
    configmethod = lambda chart: getattr(chart, 'configure_'+name)

    chart1 = Chart(config=Config( **{name:klass(**kwds)} ))
    chart2 = Chart().configure( **{name:klass(**kwds)} )
    chart3 = configmethod(Chart())(**kwds)

    assert chart1.to_dict() == chart2.to_dict()
    assert chart2.to_dict() == chart3.to_dict()


def test_config_facet_grid():

    kwds = dict(opacity=0.5, color='red')

    chart1 = Chart(
        config=Config(
            facet=FacetConfig(grid=FacetGridConfig(**kwds))
        )
    )
    chart2 = Chart().configure_facet_grid(**kwds)

    assert chart1.to_dict() == chart2.to_dict()


def test_data_finalization():
    data = pd.DataFrame({'x': np.arange(5),
                         'y': pd.date_range('2016-01-01', freq='D', periods=5),
                         'row': list('ABABA')})
    # Facet containing data and a chart
    chart1 = Chart().mark_point().encode(x='x', y='y')
    facet = FacetedChart(data, spec=chart1).set_facet(row='row')
    D = facet.to_dict()
    assert D['facet']['row']['type'] == 'nominal'
    assert D['spec']['encoding']['x']['type'] == 'quantitative'
    assert D['spec']['encoding']['y']['type'] == 'temporal'

    # Facet containing a chart and no data
    chart1 = Chart().mark_point().encode(x='x', y='y')
    facet = FacetedChart(spec=chart1).set_facet(row='row')
    D = facet.to_dict()
    assert 'type' not in D['facet']['row']
    assert 'type' not in D['spec']['encoding']['x']
    assert 'type' not in D['spec']['encoding']['y']

    # Facet containing data and a layer
    chart1 = Chart().mark_point().encode(x='x', y='y')
    chart2 = Chart().mark_rule().encode(x='average(x)', y='average(y)')
    layer = LayeredChart(layers=[chart1, chart2])
    facet = FacetedChart(data, spec=layer).set_facet(row='row')
    D = facet.to_dict()
    assert D['facet']['row']['type'] == 'nominal'
    for layer in D['spec']['layers']:
        assert layer['encoding']['x']['type'] == 'quantitative'
        assert layer['encoding']['y']['type'] == 'temporal'

    # Facet containing a layer and no data
    chart1 = Chart().mark_point().encode(x='x', y='y')
    chart2 = Chart().mark_rule().encode(x='average(x)', y='average(y)')
    layer = LayeredChart(layers=[chart1, chart2])
    facet = FacetedChart(spec=layer).set_facet(row='row')
    D = facet.to_dict()
    assert 'type' not in D['facet']['row']
    for layer in D['spec']['layers']:
        assert 'type' not in layer['encoding']['x']
        assert 'type' not in layer['encoding']['y']


SAMPLE_CODE = """
Chart(cars).mark_tick().encode(
    x='Miles_per_Gallon',
    y='Origin',
)
"""

@pytest.fixture
def sample_code():
    # In Py2, output strings will be unicode
    if PY2:
        return SAMPLE_CODE.replace("='", "=u'").strip()
    else:
        return SAMPLE_CODE.strip()


@pytest.mark.skipif(not connection_ok(), reason="No Internet Connection")
def test_finalize(sample_code):
    cars = load_dataset('cars')

    # Test that finalize is not called for ``to_python()`` method
    obj = eval(sample_code)

    assert obj.to_python(data='cars') == sample_code

    # Confirm that _finalize() changes the state
    assert obj.encoding.x.type is jst.undefined
    obj._finalize()
    assert obj.encoding.x.type is not jst.undefined

    # Confirm that finalized object contains correct type information
    D = obj.to_dict(data=False)
    assert D['encoding']['x']['type'] == 'quantitative'
    assert D['encoding']['y']['type'] == 'nominal'


def test_layered_chart_iadd():
    data = pd.DataFrame({'x':np.random.rand(10), 'y':np.random.rand(10)})
    l1 = Chart().mark_line().encode(x='x', y='y')
    l2 = Chart().mark_point().encode(x='x', y='y')

    chart = LayeredChart(data)
    chart += l1
    chart += l2
    chart2 = LayeredChart(data)
    chart2.set_layers(l1, l2)
    assert chart.to_dict()==chart2.to_dict()


def test_chart_add():
    data = pd.DataFrame({'x':np.random.rand(10), 'y':np.random.rand(10)})
    l1 = Chart(data).mark_line().encode(x='x', y='y')
    l2 = Chart(data).mark_point().encode(x='x', y='y')

    chart = l1+l2
    chart2 = LayeredChart()
    chart2.set_layers(l1, l2)
    assert chart.to_dict()==chart2.to_dict()


def test_chart_to_json():
    data = pd.DataFrame({'x':np.random.rand(10), 'y':np.random.rand(10)})
    chart = Chart(data).mark_line().encode(x='x', y='y')

    import json
    assert chart.to_dict() == json.loads(chart.to_json())


def test_chart_serve():
    from altair.utils.server import MockServer

    data = pd.DataFrame({'x':np.random.rand(10), 'y':np.random.rand(10)})
    chart = Chart(data).mark_line().encode(x='x', y='y')

    chart.serve(open_browser=False, http_server=MockServer)


def test_formula_expression():
     formula = Formula('blah', expr.log(expr.df.value) // expr.LN10)
     assert formula.field == 'blah'
     assert formula.expr == '(log(datum.value)/LN10)'


def test_filter_expression():
    transform = Transform(filter=(expr.df.value < expr.log(2)))
    assert transform.filter == "(datum.value<log(2))"


def test_df_formula():
    # create a formula the manual way
    chart1 = Chart('data.json').mark_line().encode(
        x='x',
        y='y'
    ).transform_data(
        calculate=[Formula('y', 'sin(((2*PI)*datum.x))')]
    )

    # create a formula with the dataframe interface
    df = expr.DataFrame('data.json')
    df['y'] = expr.sin(2 * expr.PI * df.x)
    chart2 = Chart(df).mark_line().encode(
        x='x',
        y='y'
    )

    # make sure the outputs match
    assert chart1.to_dict() == chart2.to_dict()


def test_df_filter():
    # create a filter the manual way
    chart1 = Chart('data.json').mark_point().encode(
        x='x',
        y='y'
    ).transform_data(
        filter='(datum.x<2)'
    )

    # create a filter with the dataframe interface
    df = expr.DataFrame('data.json')
    df = df[df.x < 2]
    chart2 = Chart(df).mark_point().encode(
        x='x',
        y='y',
    )

    # make sure outputs match
    assert chart1.to_dict() == chart2.to_dict()


def test_df_filter_multiple():
    # create a filter the manual way
    chart1 = Chart('data.json').mark_point().encode(
        x='x',
        y='y'
    ).transform_data(
        filter=['(datum.x<2)','(datum.y>4)']
    )

    # use the dataframe interface to create *two* filters
    df = expr.DataFrame('data.json')
    df = df[df.x < 2]
    df = df[df.y > 4]
    chart2 = Chart(df).mark_point().encode(
        x='x',
        y='y',
    )

    # make sure outputs match
    assert chart1.to_dict() == chart2.to_dict()


def test_chart_dir():
    # test that the dir() method of top-level objects (and by extension the
    # IPython tab-completion) exposes what we want to have exposed.
    chart = dir(Chart())
    layerchart = dir(LayeredChart())
    facetchart = dir(FacetedChart())

    for L in [chart, layerchart, facetchart]:
        # T.HasTraits methods should not appear
        assert 'has_own_traits' not in L
        # TopLevel methods should appear
        assert 'to_html' in L
        # Common traits should appear
        assert 'config' in L

    # Specialized chart methods should appear
    assert 'mark_point' in chart
    assert 'set_layers' in layerchart
    assert 'set_facet' in facetchart

    # traits should appear
    assert 'mark' in chart
    assert 'layers' in layerchart
    assert 'facet' in facetchart


def test_empty_traits():
    # regression test for #264
    axis = Axis(title='')
    assert axis.to_dict() == {'title': ''}

    # regression test for changes in #265
    assert Transform().to_dict() == {}  # filter not present


def test_max_rows():
    chart = make_chart()
    assert isinstance(chart.to_dict(), dict)
    chart.max_rows = 5
    with pytest.raises(MaxRowsExceeded):
        chart.to_dict()
    chart.max_rows = 15
    d = chart.to_dict()
    assert isinstance(d, dict)
    assert 'max_rows' not in d


def test_schema_url():
    chart = make_chart()

    # Make sure that $schema is added to the output
    dct = chart.to_dict()
    assert '$schema' in dct
    assert dct['$schema'] == schema.vegalite_schema_url

    # Make sure that $schema
    chart = Chart.from_dict(dct)


def test_enable_mime_rendering():
    # Make sure these functions are safe to call multiple times.
    enable_mime_rendering()
    enable_mime_rendering()
    disable_mime_rendering()
    disable_mime_rendering()


def test_validate_spec():

    # Make sure we catch channels with no field specified
    c = make_chart()
    c.encode(Color())
    assert isinstance(c.to_dict(), dict)
    assert isinstance(c.to_dict(validate_columns=False), dict)
    with pytest.raises(FieldError):
        c.to_dict(validate_columns=True)
    c.validate_columns = False
    assert isinstance(c.to_dict(validate_columns=True), dict)

    # Make sure we catch encoded fields not in the data
    c = make_chart()
    c.encode(x='x', y='y', color='z')
    c.encode(color='z')
    assert isinstance(c.to_dict(), dict)
    assert isinstance(c.to_dict(validate_columns=False), dict)
    with pytest.raises(FieldError):
        c.to_dict(validate_columns=True)
    c.validate_columns = False
    assert isinstance(c.to_dict(validate_columns=True), dict)
    
    c = make_chart()
    c.encode(x='x', y='count(*)')
    assert isinstance(c.to_dict(validate_columns=True), dict)

    # Make sure we can resolve computed fields
    c = make_chart()
    c.encode(x='x', y='y', color='z')
    c.encode(color='z')
    c.transform_data(
        calculate=[Formula('z', 'sin(((2*PI)*datum.x))')]
    )
    assert isinstance(c.to_dict(), dict)
