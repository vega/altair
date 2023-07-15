try:
    import anywidget  # noqa: F401
    from .chart_widget import ChartWidget
except ImportError:
    # When anywidget isn't available, create stand-in ChartWidget class
    # that raises an informative import error on construction. This
    # way we can make ChartWidget available in the altair namespace
    # when anywidget is not installed
    class ChartWidget:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "The Altair ChartWidget requires the anywidget \n"
                "Python package which may be installed using pip with\n"
                "    pip install anywidget\n"
                "or using conda with\n"
                "    conda install -c conda-forge anywidget"
            )
