import confuse
import pkg_resources

from os import path, environ

# ==========
# HARD CODED
# ==========

config_files = [
    'api.conf.yml',
    'internal.conf.yml'
]

APPNAME = 'webserver'


# CONFIG SETUP
config = confuse.Configuration(APPNAME, __name__)

for file in config_files:

    # file_path = pkg_resources.resource_filename(__name__, file)
    file_path = path.join(environ['GASH_CONFIG'], file)
    config.set_file(file_path)
    print(f'[Gashokoru_web] Configuration file added from {file_path}')