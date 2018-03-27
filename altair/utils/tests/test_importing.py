import pytest

import pandas as pd

from ..importing import attempt_import


def test_import_module():
    pandas = attempt_import('pandas', "Pandas package is not installed")
    assert pandas is pd

    with pytest.raises(RuntimeError) as err:
        attempt_import('a_module_which_should_not_exist',
                       'this module does not exist')
    assert(str(err.value) == 'this module does not exist')
