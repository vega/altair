import pytest

from altair.utils.html import spec_to_html


@pytest.fixture
def spec():
    return {
        "data": {"url": "data.json"},
        "mark": {"type": "point"},
        "encoding": {
            "x": {"field": "x", "type": "quantitative"},
            "y": {"field": "y", "type": "quantitative"},
        },
    }


@pytest.mark.parametrize("requirejs", [True, False])
@pytest.mark.parametrize("fullhtml", [True, False])
def test_spec_to_html(requirejs, fullhtml, spec):
    # We can't test that the html actually renders, but we'll test aspects of
    # it to make certain that the keywords are respected.
    vegaembed_version = "3.12"
    vegalite_version = "3.0"
    vega_version = "4.0"

    html = spec_to_html(
        spec,
        mode="vega-lite",
        requirejs=requirejs,
        fullhtml=fullhtml,
        vegalite_version=vegalite_version,
        vegaembed_version=vegaembed_version,
        vega_version=vega_version,
    )
    html = html.strip()

    if fullhtml:
        assert html.startswith("<!DOCTYPE html>")
        assert html.endswith("</html>")
    else:
        assert html.startswith("<style>")
        assert html.endswith("</script>")

    if requirejs:
        assert "require(" in html
    else:
        assert "require(" not in html

    assert f"vega-lite@{vegalite_version}" in html
    assert f"vega@{vega_version}" in html
    assert f"vega-embed@{vegaembed_version}" in html


def test_spec_to_html_olli(spec):
    html = spec_to_html(
        spec,
        mode="vega-lite",
        vegalite_version="6.0",
        vegaembed_version="7",
        vega_version="6",
        template="olli",
    )

    assert "olli@3" in html
    assert "+esm" in html
    assert "styles.css" in html
    assert "olliVis" in html
    assert "connectOlliToVegaLite" in html
    assert "withExternalStateParam" in html
    assert "looksLikeFips" in html
    assert "enrichWithUSGeo" in html
    assert "olli-adapters@" not in html
