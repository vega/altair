import six


if six.PY2:
    import BaseHTTPServer as server
    from StringIO import StringIO as IO
else:
    from http import server
    from io import BytesIO as IO


__all__ = (
    "server",
    "IO"
)
