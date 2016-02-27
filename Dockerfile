# nodev container
#
# 1. Fill the requirements.txt file.
# 2. Create your nodev docker image once with:
#   docker build -t nodev .
# 3. Run the tests with:
#   docker run --rm -it -v `pwd`:/src nodev
#
FROM python:3

# setup pytest user
RUN adduser --disabled-password --gecos "" --uid 7357 pytest
COPY ./ /src
WORKDIR /src

# setup the python and pytest environments
ENV PYTEST_NODEV_MODE=FEARLESS
RUN pip install --upgrade pip setuptools pytest-nodev -r requirements.txt

# fix up broken stdlib-list permissions, see:
#   https://github.com/jackmaney/python-stdlib-list/issues/2
RUN chmod go+r -R /usr/local/lib/python3.5/site-packages/stdlib*

# setup entry point
USER pytest
ENTRYPOINT ["py.test"]
CMD ["--wish-from-all"]
