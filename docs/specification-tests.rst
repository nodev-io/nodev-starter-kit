
Specification Tests
===================

    "If it's not tested, it's broken." - Bruce Eckel.

Testing assure you that the code works... at least in one very specific case.


Why do we love unit tests?
--------------------------

We love unit tests because they...

- help writing better code in the first place
- make refactoring possible
- keep internal API tidy
- help design and document the intended behaviour of the code


Why do we hate unit tests?
--------------------------

We hate unit tests because they...

- need as much work as code
- need to be refactored during a refactoring
- break when you change trivial implementation details
- risk keeping the focus on the process, not on the product

Feature vs. implementation
--------------------------



How to test for a feature without knowing the implementation?
-------------------------------------------------------------


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
