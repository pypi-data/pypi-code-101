import os
import time
import warnings

import docker
import requests
from elasticsearch.exceptions import ElasticsearchWarning
from get_port import find_free_port

from pytest_with_docker import container_exists, network_exists
from .defines import PYTEST_WITH_DOCKER_ES_IMAGE_NAME, \
    PYTEST_WITH_DOCKER_ES_CONTAINER_NAME, \
    PYTEST_WITH_DOCKER_ES_PORT_ENV_KEY, PYTEST_WITH_DOCKER_ES_HOST_ENV_KEY
from ..defines import PYTEST_WITH_DOCKER_NETWORK_NAME


def setup_function():
    warnings.resetwarnings()
    warnings.simplefilter('ignore', ElasticsearchWarning)

    # set host
    _es_host = '127.0.0.1'

    # find free port for elasticsearch
    _es_port = find_free_port()[0]

    # create docker client
    _client = docker.from_env()

    # docker pull elasticsearch
    _client.images.pull(os.environ.get("PYTEST_WITH_DOCKER_ES_IMAGE_NAME",
                                       default=PYTEST_WITH_DOCKER_ES_IMAGE_NAME))

    # get docker containers
    _containers = _client.containers.list(all=True)

    if container_exists(os.environ.get("PYTEST_WITH_DOCKER_ES_CONTAINER_NAME",
                                       default=PYTEST_WITH_DOCKER_ES_CONTAINER_NAME),
                        containers=_containers):

        # get container
        _container = _client.containers.get(
            os.environ.get("PYTEST_WITH_DOCKER_ES_CONTAINER_NAME",
                           default=PYTEST_WITH_DOCKER_ES_CONTAINER_NAME))

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
    if not network_exists(os.environ.get("PYTEST_WITH_DOCKER_NETWORK_NAME",
                                         default=PYTEST_WITH_DOCKER_NETWORK_NAME),
                          networks=_networks):
        _client.networks.create(
            os.environ.get("PYTEST_WITH_DOCKER_NETWORK_NAME",
                           default=PYTEST_WITH_DOCKER_NETWORK_NAME),
            driver="bridge")

    # run elasticsearch
    _container = _client.containers.run(
        command="",
        detach=True,
        environment={"discovery.type": "single-node"},
        image=os.environ.get("PYTEST_WITH_DOCKER_ES_IMAGE_NAME",
                             default=PYTEST_WITH_DOCKER_ES_IMAGE_NAME),
        name=os.environ.get("PYTEST_WITH_DOCKER_ES_CONTAINER_NAME",
                            default=PYTEST_WITH_DOCKER_ES_CONTAINER_NAME),
        network=os.environ.get("PYTEST_WITH_DOCKER_NETWORK_NAME",
                               default=PYTEST_WITH_DOCKER_NETWORK_NAME),
        ports={f'9200/tcp': _es_port}
    )

    # set elasticsearch port to environment.
    os.environ[os.environ.get("PYTEST_WITH_DOCKER_ES_HOST_ENV_KEY",
                              default=PYTEST_WITH_DOCKER_ES_HOST_ENV_KEY)] = str(
        _es_host)

    # set elasticsearch port to environment.
    os.environ[os.environ.get("PYTEST_WITH_DOCKER_ES_PORT_ENV_KEY",
                              default=PYTEST_WITH_DOCKER_ES_PORT_ENV_KEY)] = str(
        _es_port)

    # wait for launch.
    while True:
        try:
            requests.get(f'http://{_es_host}:{_es_port}', timeout=(1.0, 1.0))
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)


if __name__ == "__main__":
    # execute only if run as a script
    setup_function()

# EOF
