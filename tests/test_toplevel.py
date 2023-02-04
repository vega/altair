import altair as alt


def test_completeness_of_all():
    expected = sorted(
        [
            x
            for x in alt.__dict__.keys()
            if not getattr(getattr(alt, x), "_deprecated", False)
            and not x.startswith("__")
        ]
    )

    # If the assert statement fails below, there are probably either new objects
    # in the top-level Altair namespace or some were removed.
    # This can for example happen if Altair is updated to a new version of Vega-Lite.
    # In that case, replace the list __all__ in altair/__init__.py with what is
    # present in `expected` in this test
    assert getattr(alt, "__all__") == expected
