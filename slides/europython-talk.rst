:title: Test-driven code search and reuse coming to Python with pytest-nodev
:data-transition-duration: 500
:author: Alessandro Amici
:css: tutorial.css

.. title:: Test-driven code search and reuse coming to Python with pytest-nodev

----

Test-driven code search and reuse coming to Python with pytest-nodev
--------------------------------------------------------------------

Alessandro Amici - @alexamici

B-Open Solutions - http://bopen.eu

----

Test-driven code search
-----------------------

- **Search engine**: **pytest-nodev** is a pytest plugin that enables searching
  for code in all installed packages.
- **Search query**: the **specification test** function asserts
  the expected behaviour of the searched code.
- **Search results**: the list of the functions and classes that **PASSED** the
  *specification test*.

    .. code-block::

        http://pytest-nodev.readthedocs.io

----

The ``candidate`` fixture
-------------------------

*Specification tests* need to use the ``candidate`` fixture
provided by *pytest-nodev* and by doing so they will effectively be parametrized
by all the callables in the current environment, typically a few thousands.

This means that every *specification test* will be executed thousands of times,
once for every callable with the ``candidate`` variable holding a reference to it.

----

My first search
---------------

Let's search for a function that given the name of an executable returns
the path to it.

Let's write the *specification test* function as:

.. code-block:: python

    def test_which(candidate):
        # rename `candidate` to a more readable name
        which = candidate

        assert which('sh') == '/bin/sh'
        assert which('env') == '/usr/bin/env'

----

:id: my-first-result

My first result
---------------

.. code-block:: console

    $ py.test --candidates-from-all tests/test_which.py
    ====================== test session starts ========================
    platform linux -- Python 3.5.2, pytest-2.9.2, [...]
    rootdir: /src/tests, inifile:
    plugins: timeout-1.0.0, nodev-1.0.1
    collected 6007 items

    tests/test_which.py xxx[...]xxxXxxx[...]xxxXxxx[...]xxxXxxx[...]xxx

    =================== pytest_nodev: 3 passed ========================

    test_which.py::test_which[distutils.spawn:find_executable] PASSED
    test_which.py::test_which[pexpect.utils:which] PASSED
    test_which.py::test_which[shutil:which] PASSED

    == 6004 xfailed, 3 xpassed, 420 pytest-warnings in 109.88 seconds =
    $

----

The art of writing *specification tests*
----------------------------------------

Good *specification tests* strive to assert features and behaviours in
an implementation-agnostic way by (ab)using:

- Python dynamic nature, e.g. duck typing, the ``in`` operator, the ``==`` operator, etc.
- pytest flexibility, e.g. parametrization.
- specific helper packages, e.g. **nodev.specs**.

    .. code-block::

        http://github.com/nodev-io/nodev.specs

----

Search ``rfc3986_parse``
------------------------

Let's search a function to parse a RFC 3986 URI into tokens.

.. code-block:: python

    def test_rfc3986_parse_naive(candidate):
        rfc3986_parse = candidate

        uri = 'postgresql://user@example.com:80/path/id?q=value'
        tokens = rfc3986_parse(uri)

        # the ``in`` operator is broken for ``str``
        assert not isinstance(tokens, str)
        assert 'postgresql' in tokens
        assert '/path/id' in tokens

----

Search ``rfc3986_parse``
------------------------

More independent from implementation with *nodev.specs*:

.. code-block:: python

    from nodev.specs.generic import FlatContainer

    def test_rfc3986_parse_nodev(candidate):
        rfc3986_parse = candidate

        uri = 'postgresql://user@example.com:80/path/id?q=value'
        tokens = FlatContainer(rfc3986_parse(uri))

        assert 'postgresql' in tokens
        assert '/path/id' in tokens

----

Search ``parse_datetime``
-------------------------

