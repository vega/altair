import sys
from os.path import abspath, join, dirname

import altair as alt

current_dir = dirname(__file__)
sys.path.insert(0, abspath(join(current_dir, "..")))
from tools import update_init_file


def test_completeness_of__all__():
    relevant_attributes = [
        x for x in alt.__dict__ if update_init_file._is_relevant_attribute(x)
    ]
    relevant_attributes.sort()

    # If the assert statement fails below, there are probably either new objects
    # in the top-level Altair namespace or some were removed.
    # In that case, run tools/update_init_file.py to update __all__
    assert getattr(alt, "__all__") == relevant_attributes
