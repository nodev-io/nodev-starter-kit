nodev-starter-kit
=================

Starter-kit for nodev test-driven source code search.

Docker setup
------------

Fill the requirements.txt file.

Build the docker image once with::

    docker build -t nodev .

Run the tests with::

    docker run --rm -it -v `pwd`:/src nodev [PYTEST_OPTIONS]
