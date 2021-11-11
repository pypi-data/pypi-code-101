from testcontainers.general import DockerContainer
from testcontainers.core.waiting_utils import wait_container_is_ready
import requests


@wait_container_is_ready()
def get_exposed_port(container: DockerContainer, port: int):
    return container.get_exposed_port(port)


@wait_container_is_ready()
def wait_for_status_code(url, status):
    return requests.get(url).status_code == status


def get_bridge_ip(container: DockerContainer) -> str:
    """
    Returns the IP address of the container on the default bridge network.
    :param container: a docker container.
    :return: an IP address.
    """
    return container.get_docker_client().bridge_ip(container.get_wrapped_container().id)
