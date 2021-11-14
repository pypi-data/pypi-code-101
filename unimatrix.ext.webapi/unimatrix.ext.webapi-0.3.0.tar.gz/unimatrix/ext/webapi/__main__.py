# pylint: skip-file
import argparse
import os

import uvicorn
from unimatrix.conf import settings
from unimatrix.lib import environ

from .asgi import Application


HTTP_ASGI_MODULE = os.getenv('HTTP_ASGI_MODULE')
Application = HTTP_ASGI_MODULE if HTTP_ASGI_MODULE else Application
HTTP_PORT = os.getenv('HTTP_PORT') or 8000
HTTP_HOST = os.getenv('HTTP_HOST') or '0.0.0.0' # nosec
OPENID_SERVERS = environ.parselist(os.environ, 'OPENID_SERVERS', sep=';')


if __name__ == '__main__':
    uvicorn.run(
        Application(
            enable_debug_endpoints=True,
            root_path=os.getenv('HTTP_MOUNT_PATH'),
        ),
        host=HTTP_HOST,
        forwarded_allow_ips=os.getenv('FORWARDED_ALLOW_IPS'),
        port=HTTP_PORT,
    )
