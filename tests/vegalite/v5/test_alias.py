import pytest

import altair.vegalite.v5 as alt


def test_aliases():
    """Ensure that any aliases defined in `api.py` aren't colliding with names already defined in `core.py` or `channels.py`."""
    for alias in ["Bin", "Impute", "Title"]:
        # this test pass if the alias can resolve to its real name
        try:
            getattr(alt, alias)
        except AttributeError as err:
            raise AssertionError(f"cannot resolve '{alias}':, {err}") from err

        # this test fails if the alias match a colliding name in core
        with pytest.raises(AttributeError):
            getattr(alt.core, alias)

        # this test fails if the alias match a colliding name in channels
        with pytest.raises(AttributeError):
            getattr(alt.channels, alias)
