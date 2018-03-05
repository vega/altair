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
    try:
        return importlib.import_module(module)
    except ImportError:
        raise RuntimeError(error_message)
