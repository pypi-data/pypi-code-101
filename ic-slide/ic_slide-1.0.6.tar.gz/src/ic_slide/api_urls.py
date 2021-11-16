from .config import get_config, is_client_grant


def urljoin(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """
    return "/".join(map(lambda x: str(x).rstrip('/'), args))


def get_metadata_url(id):
    host_url = get_config("APP_API_URL")
    return urljoin(host_url,
                   f"api/app/slide/{id}/metadata")


def get_tile_url(id):
    host_url = get_config("APP_API_URL")
    return urljoin(host_url,
                   f"api/app/slide/{id}/tile")
