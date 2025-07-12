"""Test http server."""

from altair.utils.server import MockServer, serve
from tests import slow


@slow
def test_serve():
    html = "<html><title>Title</title><body><p>Content</p></body></html>"
    serve(html, open_browser=False, http_server=MockServer)
