
from __future__ import print_function

import subprocess
import sys


DOCKER_CREATE_IN = 'docker create -it nodev {}'
DOCKER_SIMPLE_CMD_IN = 'docker {} {container_id}'


def nodev(argv=()):
    container_id = subprocess.check_output(DOCKER_CREATE_IN.format(' '.join(argv)), shell=True).decode('utf-8').strip()
    print('created container: {container_id}'.format(**locals()))
    try:
        subprocess.check_call('docker cp . {container_id}:/src '.format(**locals()), shell=True)
        subprocess.check_call('docker start -ai {container_id}'.format(**locals()), shell=True)
    finally:
        print('removing container: {container_id}'.format(**locals()))
        subprocess.check_output(DOCKER_SIMPLE_CMD_IN.format('rm -f', **locals()), shell=True)


if __name__ == '__main__':
    try:
        nodev(sys.argv)
    except (subprocess.CalledProcessError, KeyboardInterrupt) as ex:
        print(ex.args)
        sys.exit(1)
