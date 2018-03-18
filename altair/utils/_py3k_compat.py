import sys

PY2 = sys.version_info[0] == 2
PY3 = not PY2

if PY2:
    from urllib2 import URLError, HTTPError, urlopen
    from urllib import urlretrieve
    string_types = basestring,
    integer_types = (int, long)
    import BaseHTTPServer as server
    from StringIO import StringIO as IO
else:
    from urllib.error import URLError, HTTPError
    from urllib.request import urlopen, urlretrieve
    string_types = str,
    integer_types = int,
    from http import server
    from io import BytesIO as IO
