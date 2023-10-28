from types import ModuleType
from packaging.version import Version
from importlib.metadata import version as importlib_version


def import_vegafusion() -> ModuleType:
    min_version = "1.4.0"
    try:
        version = importlib_version("vegafusion")
        if Version(version) < Version(min_version):
            raise ImportError(
                f"The vegafusion package must be version {min_version} or greater. "
                f"Found version {version}"
            )
        import vegafusion as vf  # type: ignore

        return vf
    except ImportError as err:
        raise ImportError(
            'The "vegafusion" data transformer and chart.transformed_data feature requires\n'
            f"version {min_version} or greater of the 'vegafusion-python-embed' and 'vegafusion' packages.\n"
            "These can be installed with pip using:\n"
            f'    pip install "vegafusion[embed]>={min_version}"\n'
            "Or with conda using:\n"
            f'    conda install -c conda-forge "vegafusion-python-embed>={min_version}" '
            f'"vegafusion>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def import_vl_convert() -> ModuleType:
    min_version = "0.14.0"
    try:
        version = importlib_version("vl-convert-python")
        if Version(version) < Version(min_version):
            raise ImportError(
                f"The vl-convert-python package must be version {min_version} or greater. "
                f"Found version {version}"
            )
        import vl_convert as vlc

        return vlc
    except ImportError as err:
        raise ImportError(
            f"The vl-convert Vega-Lite compiler and image export feature requires\n"
            f"version {min_version} or greater of the 'vl-convert-python' package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "vl-convert-python>={min_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "vl-convert-python>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def import_pyarrow_interchange() -> ModuleType:
    min_version = "11.0.0"
    try:
        version = importlib_version("pyarrow")

        if Version(version) < Version(min_version):
            raise ImportError(
                f"The pyarrow package must be version {min_version} or greater. "
                f"Found version {version}"
            )
        import pyarrow.interchange as pi

        return pi
    except ImportError as err:
        raise ImportError(
            f"Usage of the DataFrame Interchange Protocol requires\n"
            f"version {min_version} or greater of the pyarrow package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "pyarrow>={min_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "pyarrow>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def pyarrow_available() -> bool:
    try:
        import_pyarrow_interchange()
        return True
    except ImportError:
        return False
