# nodev container
#
# Fill the requirements.txt file.
#
# Build the docker image once with:
#
#   docker build -t nodev .
#
# Run the tests with:
#
#   docker run --rm -it -v `pwd`:/src nodev [PYTEST_OPTIONS]
#
FROM python:3

# setup workdir
COPY ./ /src
WORKDIR /src

# setup the python and pytest environments
RUN pip install --upgrade pip setuptools pytest-nodev
# several packages need NumPy during setup, install it unconditionally
RUN pip install --upgrade numpy
RUN pip install --upgrade -r requirements.txt
ENV PYTEST_NODEV_MODE=FEARLESS

# setup pytest user
RUN adduser --disabled-password --gecos "" --uid 7357 pytest
USER pytest

# setup entry point
ENTRYPOINT ["py.test"]
CMD ["--candidates-from-all"]
