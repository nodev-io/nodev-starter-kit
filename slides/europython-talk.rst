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

:id: search-skip-comments

Search ``skip_comments``
------------------------

.. code-block:: python

    import io
    import pytest
    from nodev.specs.generic import FlatContainer

    @pytest.mark.parametrize('text2stream', [
        lambda x: x,
        lambda x: x.splitlines(True),
        lambda x: enumerate(x.splitlines(True), 1),
        lambda x: io.StringIO(x),
    ])
    def test_skip_comments(candidate, text2stream):
        skip_comments = candidate

        text = 'value = 1 # comment\n'
        assert 'value = 1' in FlatContainer(skip_comments(text2stream(text)))
        assert 'comment' not in FlatContainer(skip_comments(text2stream(text)))

----

Search results and refinement strategies
----------------------------------------

- **only relevant results**: your *search query* is just perfect
- **no result at all**: your *search query* may be too strict

  - try relaxing your *specification tests*,
    e.g. drop corner cases or try to focus on a reduced / partial feature
  - try collecting more candidates from more code

- **no relevant result**: your *feature specification tests* is too weak

  - harden your *specification tests*, e.g. add more normal cases, add more corner cases

Defeat is when you only seem to go from *no result at all* to *no relevant result* and back.

----

Bibliography
------------

- "CodeGenie: a tool for test-driven source code search", O.A. Lazzarini Lemos *et al*,
  Companion to the 22nd ACM SIGPLAN conference on Object-oriented programming systems and applications companion,
  917--918, **2007**, ACM, http://dx.doi.org/10.1145/1297846.1297944
- "Code conjurer: Pulling reusable software out of thin air", O. Hummel *et al*,
  IEEE Software, (25) 5 45-52, **2008**, IEEE, http://dx.doi.org/10.1109/MS.2008.110
- "Finding Source Code on the Web for Remix and Reuse", S.E. Sim *et al*, 251, **2013** ---
  `PDF <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.308.2645&rep=rep1&type=pdf>`__
- "Test-Driven Reuse: Improving the Selection of Semantically Relevant Code", M. Nurolahzade,
  Ph.D. thesis, **2014**, UNIVERSITY OF CALGARY ---
  `PDF <http://lsmr.org/docs/nurolahzade_phd_2014.pdf>`__

----

Test-driven code reuse
----------------------

*Test-driven reuse* (TDR) is an extension of the *test-driven development* (TDD)
development practice.

Developing a new feature in TDR starts with the developer writing the tests
that will validate the correct implementation of the desired functionality.

Before writing any functional code the tests are used to search for a suitable
implementation.

Any code passing the tests is presented to the developer
as a candidate implementation for the target feature.

----

Test-driven code reuse
----------------------

- when no suitable code is found
  the developer needs to implement the feature and TDR reduces to TDD
- when suitable code is found the developer can:

  - **import**: accept code as a dependency and use the class / function directly
  - **fork**: copy the code and the related tests into their project
  - **study**: use the code and the related tests as guidelines for their implementation,
    in particular identifyng corner cases and optimizations

----

Unit tests validation
---------------------

An independent use case for test-driven code search is unit tests validation.

Adding ``pytest.mark.candidate`` markers does not affect your tests until you
explicitly activate *pytest-nodev* it with a ``--candidates-from-*`` option,
so you can just add the markers to your regular tests.

Once in a while you can make a search with your test as a query and
if the test passes with an unexpected object there are two possibilities,
either the test is not strict enough and allows for false positives and needs to be updated,
or the **PASSED** is actually a function you could use instead of your implementation.

----

Limitations and future work...
------------------------------

- Improve performance!
- Extend implementation independence

  - Permutate arguments, handle keyword arguments...

- Improve performance!
- Extend available code

  - Collect code from all repos, extract snippets...

- Improve performance!
- ...

----

... future work
---------------

- **Setup a web search engine!**

Trying it! Register for the beta test by sending an email to:

    .. code-block::

        nodev-test@bopen.eu

----

Conclusions
-----------

*Test-driven code search* finds code, but not any kind of code.

It tends to find very nice code, that is
code that provides features without polluting them with useless implementation details.

As long as you learn how to write good *specification tests*.

That is tests that specify a feature without insisting on useless implementation details.

----

Thanks!
-------

Alessandro Amici <a.amici@bopen.eu> - @alexamici

B-Open Solutions - http://bopen.eu

Register for beta test to:

    .. code-block::

        nodev-test@bopen.eu
