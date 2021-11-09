import os
import warnings

import docker
from elasticsearch.exceptions import ElasticsearchWarning

from pytest_with_docker import container_exists
from .defines import PYTEST_WITH_DOCKER_ES_CONTAINER_NAME


def teardown_function():
    warnings.resetwarnings()
    warnings.simplefilter('ignore', ElasticsearchWarning)

    # create docker client
    _client = docker.from_env()

    # get docker containers
    _containers = _client.containers.list()

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

    # get docker networks
    _networks = _client.networks.list()

    # prune docker network for pytest
    _client.networks.prune()


if __name__ == "__main__":
    # execute only if run as a script
    teardown_function()

# EOF
