:title: Test-driven code search and the art of writing implementation-agnostic tests
:data-transition-duration: 500
:author: Alessandro Amici
:description: The Hovercraft! tutorial.
:css: tutorial.css

.. title:: Test-driven code search and the art of writing implementation-agnostic tests

----

Test-driven code search and the art of writing implementation-agnostic tests
----------------------------------------------------------------------------

Alessandro Amici - @alexamici

B-Open Solutions - http://bopen.eu

----

Training objectives
-------------------

- Understand **test-driven code search**

  - Understand **test-driven code reuse**
  - Understand **unit tests validation**

- Practice all of the above using the **nodev** tools

  - Practice the art of writing **feature specification tests**
    as **implementation-agnostic** as possible

- Experience an epiphany about how we recognize *great code* and *great tests*

----

Training outline 1/2
--------------------

- Present the *test-driven code search* concepts
- Present and install **pytest-nodev** and **nodev-stater-kit**
- Make our first *test-driven code search*
- Practice *pytest-nodev* search options
- Present the *test-driven reuse* development strategy
- Show an example and make exercises

----

Training outline 2/2
--------------------

- Present the *feature specification tests* concepts
- Present and install **nodev.specs**
- Practice the art of writing *implementation-agnostic* test
- Present the *unit tests validation* best practice
- Show an example and make exercises
- Limitations and future work
- Conclusions

----

Training material
-----------------

Slides text::

    http://nodev-starter-kit.rtfd.io

Training repo::

    http://github.com/nodev-io/nodev-starter-kit

----

Motivation 1/4
--------------


    "Have a look at this piece of code that I'm writing--I'm sure it has been written before.
    I wouldn't be surprised to find it verbatim somewhere on GitHub." - `@kr1 <https://github.com/kr1>`_

----

Motivation 2/4
--------------

Every piece of functionality in a software project
requires code that lies somewhere in the wide reusability spectrum that goes
form extremely custom and strongly tied to the specific implementation
to completely generic and highly reusable.

On the *custom* side of the spectrum there is all the code that defines the
features of the software and all the choices of its implementation. That one is code that need
to be written.

----

Motivation 3/4
--------------

On the other hand seasoned software developers are trained to spot
pieces of functionality that lie far enough on the *generic* side of the range
that with high probability are already implemented in a **librariy** or a **framework**
and that are documented well enough to be discovered with a
**keyword-based search**, e.g. on StackOverflow and Google.

----

Motivation 4/4
--------------

In between the two extremes there is a huge gray area populated by pieces of functionality
that are not *generic* enough to obviously deserve a place in a library, but are
*common* enough that must have been already implemented by someone else for their
software. This kind of code is doomed to be re-implemented again and again
for the simple reason that **there is no way to search code by functionality**...

Or is it?

----

Test-driven code search
-----------------------

To address the limits of keyword-based search *test-driven code search*
focuses on code behaviour and semantics instead.

The **search query** is a test function that is executed once for every
candidate class or function available to the **search engine**
and the **search result** is the list of candidates that pass the test.

Due to its nature the approach is better suited for discovering smaller functions
with a generic signature.

*pytest-nodev* is a pytest plugin that enables *test-driven code search* for Python.

----

Bibliography 1/2
----------------

- "CodeGenie: a tool for test-driven source code search", O.A. Lazzarini Lemos *et al*,
  Companion to the 22nd ACM SIGPLAN conference on Object-oriented programming systems and applications companion,
  917--918, **2007**, ACM, http://dx.doi.org/10.1145/1297846.1297944

- "Code conjurer: Pulling reusable software out of thin air", O. Hummel *et al*,
  IEEE Software, (25) 5 45-52, **2008**, IEEE, http://dx.doi.org/10.1109/MS.2008.110 ---
  `PDF <http://cosc612.googlecode.com/svn/Research%20Paper/Code%20Conjurer.pdf>`__

----

Bibliography 2/2
----------------

- "Finding Source Code on the Web for Remix and Reuse", S.E. Sim *et al*, 251, **2013** ---
  `PDF <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.308.2645&rep=rep1&type=pdf>`__

- "Test-Driven Reuse: Improving the Selection of Semantically Relevant Code", M. Nurolahzade,
  Ph.D. thesis, **2014**, UNIVERSITY OF CALGARY ---
  `PDF <http://lsmr.org/docs/nurolahzade_phd_2014.pdf>`__

----

pytest-nodev
------------

pytest-nodev is a pytest plugin that implements a simple test-driven search engine for Python code,
it finds classes and functions that match the behaviour specified by the given tests.

Documentation::

    http://pytest-nodev.readthedocs.io

Development::

    https://github.com/nodev-io/pytest-nodev

Download::

    https://pypi.python.org/pypi/pytest-nodev

----

nodev-starter-kit
-----------------

nodev-starte-kit lets you perform test-driven code search queries
with `pytest-nodev <https://pypi.python.org/pypi/pytest-nodev>`_
safely and efficiently using `docker <https://docker.com>`_.

Go to::

    https://github.com/nodev-io/nodev-starter-kit

fork the repo on GitHub and git clone your fork::

    $ git clone https://github.com/$USER/nodev-starter-kit


----

FAQ 1/2
-------

**Why do I need special care to run pytest-nodev?**

Searching code with pytest-nodev looks very much like running arbitrary callables with random arguments.
A lot of functions called with the wrong set of arguments may have unexpected consequences ranging
from slightly annoying, think ``os.mkdir('false')``,
to **utterly catastrophic**, think ``shutil.rmtree('/', True)``.
Serious use of pytest-nodev, in particular using ``--candidates-from-all``,
require running the tests with operating-system level isolation,
e.g. as a dedicated user or even better inside a dedicated container.

----

FAQ 2/2
-------

**But isn't it docker overkill? Can't I just use a dedicated user to run pytest-nodev?**

We tried hard to find a simpler setup, but once all the nitty-gritty details are factored in
we choose docker as the best trade-off between safety, reproducibility and easiness of use.

----

Install docker-engine and docker
--------------------------------

In order to run pytest-nodev you need to access a docker-engine server via the docker client,
if you don't have Docker already setup
you need to follow the official installation instructions for your platform:

- `Docker for Linux <https://docs.docker.com/engine/installation/linux/>`_
- `Docker for MacOS <https://docs.docker.com/docker-for-mac/>`_
- `Docker for Windows <https://docs.docker.com/docker-for-windows/>`_

**YOU DON'T NEED TO INSTALL THE DOCKER-ENGINE SERVER FOR THE TRAINING!**

----

Create the nodev image
----------------------

The *nodev* docker image will be your search engine,
it needs to be created once and updated every time you want to
change the packages installed in the search engine environment.

With an editor fill the requirements.txt file with the packages to be installed in the search engine.

Build the docker image with::

    $ docker build -t nodev .

**YOU DON'T NEED TO CREATE THE NODEV IMAGE FOR THE TRAINING!**

----

Setup the docker client
-----------------------

Set the ``DOCKER_HOST`` environment variable to the training docker-engine server on AWS::

    $ export DOCKER_HOST="tcp://23.23.23.23:4243"

Test with::

    $ docker images
    REPOSITORY  TAG     IMAGE ID      CREATED         SIZE
    nodev       latest  26ee171c2744  18 minutes ago  802.4 MB
    [...]

----

Our first search 1/5
--------------------

We need to write a ``parse_bool`` function that robustly parses a boolean value from a string.
Here is the test we intend to use to validate our own implementation once we write it:

.. code:: python

    def test_parse_bool():
        assert not parse_bool('false')
        assert not parse_bool('FALSE')
        assert not parse_bool('0')

        assert parse_bool('true')
        assert parse_bool('TRUE')
        assert parse_bool('1')

----

Our first search 2/5
--------------------

We copy our specification test to the ``tests/test_parse_bool.py`` file and
decorate it with ``pytest.mark.candidate`` as follows:

.. code:: python

    import pytest

    @pytest.mark.candidate('parse_bool')
    def test_parse_bool():
        assert not parse_bool('false')
        assert not parse_bool('FALSE')
        assert not parse_bool('0')

        assert parse_bool('true')
        assert parse_bool('TRUE')
        assert parse_bool('1')

----

:id: first-search-3

Our first search 3/5
--------------------

And we instruct our search engine to run our test on all candidate callables in the Python standard library::

    $ python docker-nodev.py --candidates-from-stdlib tests/test_parse_bool.py
    ======================= test session starts ==========================
    [...]
    collected 4000 items

    test_parse_bool.py xxxxxxxxxxxx[...]xxxxxxxxXxxxxxxxx[...]xxxxxxxxxxxx

    ====================== pytest_nodev: 1 passed ========================

    test_parse_bool.py::test_parse_bool[distutils.util:strtobool] PASSED

    === 3999 xfailed, 1 xpassed, 260 pytest-warnings in 75.38 seconds ====

In just over a minute pytest-nodev collected 4000 functions from the standard library,
run your specification test on all of them and
reported that the `strtobool`_ function in the distutils.util module
is the only candidate that passes our test.

.. _`strtobool`: https://docs.python.org/3/distutils/apiref.html#distutils.util.strtobool

----

Our first search 4/5
--------------------

``distutils.util:strtobool``
Convert a string representation of truth to true (1) or false (0).

.. code:: python

    def strtobool (val):
        val = val.lower()
        if val in ('y', 'yes', 't', 'true', 'on', '1'):
            return 1
        elif val in ('n', 'no', 'f', 'false', 'off', '0'):
            return 0
        else:
            raise ValueError("invalid truth value %r" % (val,))

https://github.com/python/cpython/blob/3.5/Lib/distutils/util.py#L304

----

Our first search 5/5
--------------------

**Wow! Does it work so well all the times?**

Honestly no! But it's the perfect example of the benefits of *test-driven code search*

- a function imported is a one less function coded---and tested, documented, debugged,
  ported, maintained...
- it's battle tested code---lot's of old bugs have already been squashed
- it's other people code---there's an upstream to report new bugs to
- it gives you additional useful functionality---for free on top of that
- it's in the Python standard library---no additional dependency required

----

Practice pytest-nodev
---------------------

- practice command line options

  - collection options
  - includes and excludes
  - explicit fail to debug

- work around crashes
- find more ``parse_bool`` implementations

  - ``numpy.distutils.fcompiler:str2bool``
  - ``click.types:BOOL``

----

Test-driven code reuse 1/2
--------------------------

*Test-driven reuse* (TDR) is an extension of the well known *test-driven development* (TDD)
development practice.

Developing a new feature in TDR starts with the developer writing the tests
that will validate the correct implementation of the desired functionality.

Before writing any functional code the tests are run against all functions
and classes of all available projects.

Any code passing the tests is presented to the developer
as a candidate implementation for the target feature.

----

Test-driven code reuse 2/2
--------------------------

- if nothing passes the tests the developer need to implement the feature and TDR reduces to TDD
- if any code passes the tests the developer can:

  - **import**: accept code as a dependency and use the class / function directly
  - **fork**: copy the code and the related tests into their project
  - **study**: use the code and the related tests as guidelines for their implementation,
    in particular identifyng corner cases and optimizations

----

Practice TDR 1/2
----------------

Search (or implement) a ``parse_datetime`` function returning
the correct ``datetime:datetime`` object
from the following ISO 8601 strings:

.. code:: python

    '2015-06-30T23:59:59'
    '2015-06-30T23:59:59Z'
    '2015-06-30T22:59:59-01:00'
    '2015-06-30T23:59:59.623431'
    '2015-06-30T23:59:59.623431Z'
    '2015-06-30T22:59:59.623431-01:00'

----

Practice TDR 2/2
----------------

Search (or implement) a ``parse_datetime`` function returning
the correct UTC calendar tuple, e.g. ``(2015, 6, 30, 23, 59, 60.623431)``,
from the following ISO 8601 strings:

.. code:: python

    '2015-06-30T23:59:60'
    '2015-06-30T23:59:60Z'
    '2015-06-30T22:59:60-01:00'
    '2015-06-30T23:59:60.623431'
    '2015-06-30T23:59:60.623431Z'
    '2015-06-30T22:59:60.623431-01:00'

----

Limitations and future work
---------------------------

- Improve performance!
- Extend implementation independence

  - Permutate arguments, handle keyword arguments...

- Improve performance!
- Extend available code

  - Collect code from all repos, extract snippets...

- Improve performance!
- **Setup a web search engine!**

----

Conclusions
-----------

*Test-driven code search* tends to find *great code*,
code that provides features without polluting them with useless implementation details.

As long as you learn to write *great tests*,
tests that specify a feature without insisting on useless implementation details.


----

Thanks!
-------

Alessandro Amici - @alexamici

B-Open Solutions - http://bopen.eu
