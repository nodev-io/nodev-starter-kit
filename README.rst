nodev-starter-kit
=================

Starter-kit for nodev test-driven source code search.

Docker local setup
------------------

Fill the requirements.txt file.

Build the docker image once with::

    docker build -t nodev .

Run the tests with::

    docker run --rm -it -v `pwd`:/src nodev [PYTEST_OPTIONS]

Remote access to a docker server
--------------------------------

Install the docker client::

    apt install docker.io

Set the DOCKER_HOST environment variable::

    export DOCKER_HOST="tcp://xxx.xxx.xxx.xxx:4243"

Run the tests with::

    python docker-nodev.py [PYTEST_OPTIONS]
