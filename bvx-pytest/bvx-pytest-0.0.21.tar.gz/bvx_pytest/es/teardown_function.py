import warnings

import docker
from bvx_docker import container_exists
from elasticsearch.exceptions import ElasticsearchWarning

from .defines import BVX_PYTEST_DOCKER_ES_CONTAINER_NAME


def teardown_function():
    warnings.resetwarnings()
    warnings.simplefilter('ignore', ElasticsearchWarning)

    # create docker client
    _client = docker.from_env()

    # get docker containers
    _containers = _client.containers.list()

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

    # get docker networks
    _networks = _client.networks.list()

    # prune docker network for pytest
    _client.networks.prune()


if __name__ == "__main__":
    # execute only if run as a script
    teardown_function()

# EOF
