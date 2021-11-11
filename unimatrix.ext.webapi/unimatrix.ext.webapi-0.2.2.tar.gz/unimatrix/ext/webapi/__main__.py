# pylint: skip-file
import argparse
import os

import uvicorn

from .asgi import Application


HTTP_ASGI_MODULE = os.getenv('HTTP_ASGI_MODULE')
Application = ioc.loader.import_symbol(HTTP_ASGI_MODULE)\
    if HTTP_ASGI_MODULE else Application


if __name__ == '__main__':
    uvicorn.run(Application(enable_debug_endpoints=True))
