from importlib.util import find_spec
from typing import TYPE_CHECKING, NoReturn

_ANYWIDGET_IMPORT_ERROR = (
    "The Altair JupyterChart requires the anywidget \n"
    "Python package which may be installed using pip with\n"
    "    pip install anywidget\n"
    "or using conda with\n"
    "    conda install -c conda-forge anywidget\n"
    "Afterwards, you will need to restart your Python kernel."
)


def _raise_anywidget_import_error() -> NoReturn:
    raise ImportError(_ANYWIDGET_IMPORT_ERROR)


if TYPE_CHECKING:
    from .jupyter_chart import JupyterChart
elif find_spec("anywidget") is None:
    # When anywidget isn't available, create a stand-in JupyterChart class
    # that raises an informative import error when its API is used. This
    # way we can make JupyterChart available in the altair namespace
    # when anywidget is not installed.
    class JupyterChart:
        def __init__(self, *args: object, **kwargs: object) -> NoReturn:
            _raise_anywidget_import_error()

        @classmethod
        def enable_offline(cls, offline: bool = True) -> NoReturn:
            _raise_anywidget_import_error()

else:
    from .jupyter_chart import JupyterChart as JupyterChart
