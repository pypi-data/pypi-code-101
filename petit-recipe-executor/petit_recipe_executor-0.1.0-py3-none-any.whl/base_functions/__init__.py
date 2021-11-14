from requests.api import delete

from .base_functions import contains, equal, not_equal, pick
from .http_funcs import delete, get, get_ping, patch, post, put

functions = {
    "http.get": get,
    "http.post": post,
    "http.put": put,
    "http.delete": delete,
    "http.patch": patch,
    "http.ping_get": get_ping,

    # basic utils
    "pick": pick,
    "contains": contains,
    "equal": equal,
    "not_equal": not_equal,
}
