from pathlib import Path
import sys

import altair as alt

current_dir = Path(__file__).parent
sys.path.insert(0, str((current_dir / "..").resolve()))
from tools import update_init_file  # noqa: E402


def test_completeness_of__all__():
    relevant_attributes = [
        x for x in alt.__dict__ if update_init_file._is_relevant_attribute(x)
    ]
    relevant_attributes.sort()

    # If the assert statement fails below, there are probably either new objects
    # in the top-level Altair namespace or some were removed.
    # In that case, run tools/update_init_file.py to update __all__
    assert alt.__all__ == relevant_attributes
