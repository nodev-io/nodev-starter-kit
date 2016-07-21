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

Due to its nature the approach is better suited for discovering smaller functions
with a generic signature.



=============================================================================== pytest_nodev: 21 passed ===============================================================================

tests/test_parse_datetime.py::test_parse_datetime_naive[DateTime.DateTime:DateTime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[arrow.api:get] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[astropy.time.core:Time] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[botocore.utils:parse_timestamp] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[botocore.utils:parse_to_aware_datetime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[dateparser:parse] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[dateutil.parser:parse] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[delorean.interface:parse] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[fiona.rfc3339:parse_datetime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[jupyter_client.jsonutil:extract_dates] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[jupyter_client.jsonutil:parse_date] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[logbook.helpers:parse_iso8601] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[pandas.tseries.tools:parse_time_string] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[pandas.tslib:parse_datetime_string] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[pandas.tslib:parse_datetime_string_with_reso] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[yaml:load] PASSED
tests/test_parse_datetime.py::test_parse_datetime_naive[yaml:safe_load] PASSED

========================================================== 2975 xfailed, 21 xpassed, 1673 pytest-warnings in 110.80 seconds ===========================================================

=============================================================================== pytest_nodev: 15 passed ===============================================================================

tests/test_parse_datetime.py::test_parse_datetime_timezone[DateTime.DateTime:DateTime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[arrow.api:get] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[botocore.utils:parse_timestamp] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[botocore.utils:parse_to_aware_datetime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[dateutil.parser:parse] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[delorean.interface:parse] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[fiona.rfc3339:parse_datetime] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[jupyter_client.jsonutil:extract_dates] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[jupyter_client.jsonutil:parse_date] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[logbook.helpers:parse_iso8601] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[pandas.tseries.tools:parse_time_string] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[pandas.tslib:parse_datetime_string] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[pandas.tslib:parse_datetime_string_with_reso] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[yaml:load] PASSED
tests/test_parse_datetime.py::test_parse_datetime_timezone[yaml:safe_load] PASSED

========================================================== 2943 xfailed, 15 xpassed, 1672 pytest-warnings in 105.28 seconds ===========================================================

=============================================================================== pytest_nodev: 2 passed ================================================================================

tests/test_parse_datetime.py::test_parse_datetime_leap_seconds[astropy.time.core:Time] PASSED
tests/test_parse_datetime.py::test_parse_datetime_leap_seconds[fiona.rfc3339:parse_datetime] PASSED

=========================================================== 2956 xfailed, 2 xpassed, 1671 pytest-warnings in 102.16 seconds ===========================================================
