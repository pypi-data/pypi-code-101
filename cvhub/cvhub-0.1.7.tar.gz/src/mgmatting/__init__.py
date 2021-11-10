import toml

from .utils import *
from .net_engine import MGEngine


def load_config(config_path):
    with open(config_path) as f:
        utils.load_config(toml.load(f))

    # Check if toml config file is loaded
    if CONFIG.is_default:
        raise ValueError("No .toml config loaded.")
