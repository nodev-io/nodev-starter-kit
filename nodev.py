
import contextlib
import subprocess
import sys


DOCKER_CREATE_IN = 'docker create -it nodev {}'
DOCKER_CMD_IN = 'docker {} {}'


@contextlib.contextmanager
def setup_container(argv=[]):
    docker_create = DOCKER_CREATE_IN.format(' '.join(argv))
    container_id = subprocess.check_output(docker_create, shell=True).strip()
    try:
        yield container_id
    finally:
        subprocess.call(DOCKER_CMD_IN.format('kill', container_id), shell=True)
        subprocess.call(DOCKER_CMD_IN.format('rm', container_id), shell=True)


def nodev():
    with setup_container(sys.argv[1:]) as container_id:
        subprocess.check_call('docker cp . {}:/src '.format(container_id), shell=True)
        subprocess.check_call('docker start -ai {}'.format(container_id), shell=True)


if __name__ == '__main__':
    nodev()
