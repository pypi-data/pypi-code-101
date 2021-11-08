import os
import time
import warnings

import docker
import requests
from bvx_docker import network_exists, container_exists
from bvx_network import unused_port_number
from elasticsearch.exceptions import ElasticsearchWarning

from .defines import BVX_PYTEST_DOCKER_ES_IMAGE_NAME, \
    BVX_PYTEST_DOCKER_ES_CONTAINER_NAME, \
    BVX_PYTEST_DOCKER_ES_PORT_ENV_KEY
from ..defines import BVX_PYTEST_DOCKER_NETWORK_NAME


def setup_function():
    warnings.resetwarnings()
    warnings.simplefilter('ignore', ElasticsearchWarning)

    # find free port for elasticsearch
    _es_port = unused_port_number()

    # create docker client
    _client = docker.from_env()

    # docker pull elasticsearch
    _client.images.pull(BVX_PYTEST_DOCKER_ES_IMAGE_NAME)

    # get docker containers
    _containers = _client.containers.list(all=True)

    if container_exists(BVX_PYTEST_DOCKER_ES_CONTAINER_NAME,
                        containers=_containers):

        # get container
        _container = _client.containers.get(BVX_PYTEST_DOCKER_ES_CONTAINER_NAME)

        # get container status
        if _container.status == "running":
            # stop container
            _container.stop()

        # remove container
        _container.remove()

    # prune docker networks
    _client.networks.prune()

    # get docker networks
    _networks = _client.networks.list()

    # create docker network for pytest
    if not network_exists(BVX_PYTEST_DOCKER_NETWORK_NAME, networks=_networks):
        _client.networks.create(BVX_PYTEST_DOCKER_NETWORK_NAME, driver="bridge")

    # run elasticsearch
    _container = _client.containers.run(
        command="",
        detach=True,
        environment={"discovery.type": "single-node"},
        image=BVX_PYTEST_DOCKER_ES_IMAGE_NAME,
        name=BVX_PYTEST_DOCKER_ES_CONTAINER_NAME,
        network=BVX_PYTEST_DOCKER_NETWORK_NAME,
        ports={f'9200/tcp': _es_port}
    )

    # set elasticsearch port to environment.
    os.environ[BVX_PYTEST_DOCKER_ES_PORT_ENV_KEY] = str(_es_port)

    # wait for launch.
    while True:
        try:
            requests.get(f'http://127.0.0.1:{_es_port}', timeout=(10.0, 10.0))
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)


if __name__ == "__main__":
    # execute only if run as a script
    setup_function()

# EOF
