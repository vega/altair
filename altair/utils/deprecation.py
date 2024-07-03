from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if sys.version_info >= (3, 13):
    from warnings import deprecated as _deprecated
else:
    from typing_extensions import deprecated as _deprecated


if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString


class AltairDeprecationWarning(DeprecationWarning): ...


def _format_message(
    version: LiteralString,
    alternative: LiteralString | None,
    message: LiteralString | None,
    /,
) -> LiteralString:
    output = f"Deprecated in `altair={version}`."
    if alternative:
        output = f"{output} Use {alternative} instead."
    return f"{output}\n{message}" if message else output


# NOTE: Annotating the return type breaks `pyright` detecting [reportDeprecated]
# NOTE: `LiteralString` requirement is introduced by stubs
def deprecated(
    *,
    version: LiteralString,
    alternative: LiteralString | None = None,
    message: LiteralString | None = None,
    category: type[AltairDeprecationWarning] | None = AltairDeprecationWarning,
    stacklevel: int = 1,
):  # te.deprecated
    """Indicate that a class, function or overload is deprecated.

    When this decorator is applied to an object, the type checker
    will generate a diagnostic on usage of the deprecated object.

    Parameters
    ----------
    version
        ``altair`` version the deprecation first appeared.
    alternative
        Suggested replacement class/method/function.
    message
        Additional message appended to ``version``, ``alternative``.
    category
        If the *category* is ``None``, no warning is emitted at runtime.
    stacklevel
        The *stacklevel* determines where the
        warning is emitted. If it is ``1`` (the default), the warning
        is emitted at the direct caller of the deprecated object; if it
        is higher, it is emitted further up the stack.
        Static type checker behavior is not affected by the *category*
        and *stacklevel* arguments.

    References
    ----------
    [PEP 702](https://peps.python.org/pep-0702/)
    """
    msg = _format_message(version, alternative, message)
    return _deprecated(msg, category=category, stacklevel=stacklevel)
