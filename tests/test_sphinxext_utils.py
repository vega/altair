from __future__ import annotations

from typing import TYPE_CHECKING

from sphinxext.utils import get_docstring_and_rest

if TYPE_CHECKING:
    from pathlib import Path


def test_get_docstring_and_rest(tmp_path: Path) -> None:
    source = tmp_path / "example.py"
    source.write_text('"""Summary.\n\nDetails.\n"""\nchart = 1\n', encoding="utf-8")

    docstring, category, rest, lineno, is_new = get_docstring_and_rest(source)

    assert docstring == "Summary.\n\nDetails.\n"
    assert category is None
    assert rest == "chart = 1\n"
    assert lineno == 5
    assert not is_new
