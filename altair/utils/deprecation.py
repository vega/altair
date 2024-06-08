from __future__ import annotations

import sys
from typing import Callable, TypeVar, TYPE_CHECKING
import warnings
import functools

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec

if TYPE_CHECKING:
    from functools import _Wrapped

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")


class AltairDeprecationWarning(UserWarning):
    pass


def deprecated(
    message: str | None = None,
) -> Callable[..., type[T] | _Wrapped[P, R, P, R]]:
    """Decorator to deprecate a function or class.

    Parameters
    ----------
    message : string (optional)
        The deprecation message
    """

    def wrapper(obj: type[T] | Callable[P, R]) -> type[T] | _Wrapped[P, R, P, R]:
        return _deprecate(obj, message=message)

    return wrapper


def _deprecate(
    obj: type[T] | Callable[P, R], name: str | None = None, message: str | None = None
) -> type[T] | _Wrapped[P, R, P, R]:
    """Return a version of a class or function that raises a deprecation warning.

    Parameters
    ----------
    obj : class or function
        The object to create a deprecated version of.
    name : string (optional)
        The name of the deprecated object
    message : string (optional)
        The deprecation message

    Returns
    -------
    deprecated_obj :
        The deprecated version of obj

    Examples
    --------
    >>> class Foo: pass
    >>> OldFoo = _deprecate(Foo, "OldFoo")
    >>> f = OldFoo()  # doctest: +SKIP
    AltairDeprecationWarning: alt.OldFoo is deprecated. Use alt.Foo instead.
    """
    if message is None:
        message = f"alt.{name} is deprecated. Use alt.{obj.__name__} instead." ""
    if isinstance(obj, type):
        if name is None:
            msg = f"Requires name, but got: {name=}"
            raise TypeError(msg)
        else:
            return type(
                name,
                (obj,),
                {
                    "__doc__": obj.__doc__,
                    "__init__": _deprecate(obj.__init__, "__init__", message),
                },
            )
    elif callable(obj):

        @functools.wraps(obj)
        def new_obj(*args: P.args, **kwargs: P.kwargs) -> R:
            warnings.warn(message, AltairDeprecationWarning, stacklevel=1)
            return obj(*args, **kwargs)

        new_obj._deprecated = True  # type: ignore[attr-defined]
        return new_obj
    else:
        msg = f"Cannot deprecate object of type {type(obj)}"
        raise ValueError(msg)
