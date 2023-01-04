import pytest

import altair.vegalite.v5 as alt


def test_aliases():
    """Ensure that any aliases defined in `api.py` aren't colliding with names already defined in `core.py` or `channels.py`."""
    for alias in ["Bin", "Impute", "Title"]:
        getattr(alt, alias)

        with pytest.raises(AttributeError):
            getattr(alt.core, alias)

        with pytest.raises(AttributeError):
            getattr(alt.channels, alias)
