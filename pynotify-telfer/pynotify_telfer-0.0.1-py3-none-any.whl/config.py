import os

import pkg_resources
import yaml

config_file = pkg_resources.resource_filename(__name__, "config.yaml")


def load_config():
    print(config_file)
    if not os.path.exists(config_file):
        return {}

    with open(config_file, "r") as fp:
        return yaml.load(fp, yaml.FullLoader)


def write_config(config):
    with open(config_file, "w") as fp:
        yaml.dump(config, fp)
