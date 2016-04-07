
Examples
--------

Another example, find a function that decomposes a URL into individual rfc3986 components::

    $ py.test examples/test_rfc3986_parse.py --candidates-from-modules urllib.parse
    [...]
    examples/test_rfc3986_parse.py::test_rfc3986_parse_basic[urllib.parse:urlparse] HIT
    examples/test_rfc3986_parse.py::test_rfc3986_parse_basic[urllib.parse:urlsplit] HIT
    [...]

the two functions ``urlparse`` and ``urlsplit`` pass the basic rfc3986 parsing test, but do not
pass the more complex ``test_rfc3986_parse_full`` test.

More advanced functions are available on PyPI::

    $ pip install urllib3
    $ py.test examples/test_rfc3986_parse.py --candidates-from-modules urllib3
    [...]
    examples/test_rfc3986_parse.py::test_rfc3986_parse_basic[urllib3.util.url:parse_url] HIT
    examples/test_rfc3986_parse.py::test_rfc3986_parse_full[urllib3.util.url:parse_url] HIT
    [...]

now the function ``parse_url`` in the module ``urllib3.util.url`` passes both tests.
