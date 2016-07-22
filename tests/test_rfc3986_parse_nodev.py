
from nodev.specs.generic import FlatContainer

def test_rfc3986_parse_nodev(candidate):
    rfc3986_parse = candidate

    uri = 'postgresql://user@example.com:80/path/id?q=value'
    tokens = FlatContainer(rfc3986_parse(uri))

    assert 'postgresql' in tokens
    assert '/path/id' in tokens
