"""
Test http server
"""

try:
    # Python 2
    from StringIO import StringIO as IO
except:
    # Python 3
    from io import BytesIO as IO


from altair.utils.server import serve


def test_serve():
    class MockRequest(object):
        def makefile(self, *args, **kwargs):
            return IO(b"GET /")

    class MockServer(object):
        def __init__(self, ip_port, Handler):
            handler = Handler(MockRequest(), ip_port[0], self)

        def serve_forever(self):
            pass

        def server_close(self):
            pass

    html = '<html><title>Title</title><body><p>Content</p></body></html>'
    serve(html, open_browser=False, http_server=MockServer)
