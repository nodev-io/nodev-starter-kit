
def test_rfc3986_parse_naive(candidate):
    rfc3986_parse = candidate

    uri = 'postgresql://user@example.com:80/path/id?q=value'
    tokens = rfc3986_parse(uri)

    # the ``in`` operator is broken for ``str``
    assert not isinstance(tokens, str)
    assert 'postgresql' in tokens
    assert '/path/id' in tokens
