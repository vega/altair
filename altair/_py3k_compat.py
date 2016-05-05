import sys

# True if we are running on Python 3.
PY2 = sys.version_info[0] == 2

if PY2:
    string_types = basestring,
    integer_types = (int, long)
else:
    string_types = str,
    integer_types = int,
