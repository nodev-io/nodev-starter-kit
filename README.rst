
.. This document is intended as the main entry point for new users,
   it serves as the landing page on GitHub and on PyPI and
   it is also used as Quickstart section of the docs.
   Its goal are:
   * inspire and raise interest in new users
   * present one complete end-to-end use case
   * warn users of risks and suggest mitigation strategies
   * direct interested users to the appropriate project resource
   * state license and open source nature
   * credit contributors
   Anything else should go into docs.

.. NOTE: only the first couple of lines of the README are shown on GitHub mobile

nodev-starte-kit lets you perform test-driven code search queries
with `pytest-nodev <https://pypi.python.org/pypi/pytest-nodev>`_
safely and efficiently using `docker <https://docker.com>`_.

**Why do I need special care to run pytest-nodev?**

Searching code with pytest-nodev looks very much like running arbitrary callables with random arguments.
A lot of functions called with the wrong set of arguments may have unexpected consequences ranging
from slightly annoying, think ``os.mkdir('false')``,
to **utterly catastrophic**, think ``shutil.rmtree('/', True)``.
Serious use of pytest-nodev, in particular using ``--candidates-from-all``,
require running the tests with operating-system level isolation,
e.g. as a dedicated user or even better inside a dedicated container.

**But isn't it docker overkill? Can't I just use a dedicated user to run pytest-nodev?**

We tried hard to find a simpler setup, but once all the nitty-gritty details are factored in
we choosed docker as the best trade-off between safety, reproducibility and easiness of use.


Local docker setup
------------------

Fill the requirements.txt file.

Build the docker image once with::

    docker build -t nodev .

Run the tests with::

    docker run --rm -it -v `pwd`:/src nodev [PYTEST_OPTIONS]

Remote docker setup
-------------------

Install the docker client::

    apt install docker.io

Set the DOCKER_HOST environment variable::

    export DOCKER_HOST="tcp://xxx.xxx.xxx.xxx:4243"

Run the tests with::

    python docker-nodev.py [PYTEST_OPTIONS]

Project resources
-----------------

============= ======================
Documentation http://nodev-starter-kit.readthedocs.io
Support       https://stackoverflow.com/search?q=pytest-nodev
Development   https://github.com/nodev-io/nodev-starter-kit
============= ======================


Contributing
------------

Contributions are very welcome. Please see the `CONTRIBUTING`_ document for
the best way to help.
If you encounter any problems, please file an issue along with a detailed description.

.. _`CONTRIBUTING`: https://github.com/nodev-io/nodev-starter-kit/blob/master/CONTRIBUTING.rst

Authors:

- Alessandro Amici - `@alexamici <https://github.com/alexamici>`_

Sponsors:

- .. image:: http://www.bopen.it/wp-content/uploads/2016/01/logo-no-back.png
      :target: http://bopen.eu/
      :alt: B-Open Solutions srl


License
-------

nodev-starter-kit is free and open source software
distributed under the terms of the `MIT <http://opensource.org/licenses/MIT>`_ license.
