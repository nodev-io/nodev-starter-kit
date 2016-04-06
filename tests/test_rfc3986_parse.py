# -*- coding: utf-8 -*-

import pytest

@pytest.mark.candidate('rfc3986_parse')
def test_rfc3986_parse_basic():
    object_ = rfc3986_parse('postgresql://user@example.com:8080/example/path?param=value')
    tokens = list(object_)
    assert 'postgresql' in tokens
    assert '/example/path' in tokens


@pytest.mark.candidate('rfc3986_parse')
def test_rfc3986_parse_full():
    object_ = rfc3986_parse('postgresql://user@example.com:8080/example/path?param=value')
    tokens = list(object_)
    assert 'postgresql' in tokens
    assert 'user' in tokens
    assert 'example.com' in tokens
    assert 8080 in tokens or '8080' in tokens
    assert '/example/path' in tokens
