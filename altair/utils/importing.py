"""
Tools for importing dependencies
"""
import importlib


def attempt_import(module, error_message):
    """Attempt import of a dependency

    If the dependency is not available, raise a RuntimeError with the appropriate message

    Parameters
    ----------
    module : string
        the module name
    error_message : string
        the error to raise if the module is not importable

    Returns
    -------
    mod : ModuleType
        the imported module

    Raises
    ------
    RuntimeError
    """
    # Python 3.6+ raises a ModuleNotFoundError if import fails
    # Previous python versions raise an ImportError instead
    # Here we make ModuleNotFoundError = ImportError for older Python versions
    try:
        ModuleNotFoundError
    except NameError:
        ModuleNotFoundError = ImportError

    try:
        return importlib.import_module(module)
    except ModuleNotFoundError:
        raise RuntimeError(error_message)
