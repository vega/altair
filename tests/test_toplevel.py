import altair as alt

from tools import update_init_file


def test_completeness_of__all__():
    relevant_attributes = update_init_file.relevant_attributes(alt.__dict__)

    # If the assert statement fails below, there are probably either new objects
    # in the top-level Altair namespace or some were removed.
    # In that case, run tools/update_init_file.py to update __all__
    assert alt.__all__ == relevant_attributes
