import sys

PY2 = sys.version_info[0] == 2
PY3 = not PY2

if PY2:
    string_types = basestring,
    integer_types = (int, long)
else:
    string_types = str,
    integer_types = int,
