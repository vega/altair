import pytest

import altair.vegalite.v5 as alt


def test_aliases():
    """We define `Bin` to be an alias `BinParams`,  and similarly `Impute` for `ImputeParams` and `Title` for `TitleParams`.  Here we ensure that `Bin`, `Impute`, and `Title` are not already defined in `core.py` or `channels.py`."""
    for alias in ["Bin", "Impute", "Title"]:
        getattr(alt, alias)

        with pytest.raises(AttributeError):
            getattr(alt.core, alias)

        with pytest.raises(AttributeError):
            getattr(alt.channels, alias)
