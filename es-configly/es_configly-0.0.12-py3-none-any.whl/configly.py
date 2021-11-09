import json
import os
from os.path import dirname

from bvx_env import values as envs
# from elasticsearch import Elasticsearch
from bvx_es import inspect
from bvx_oop import Singleton

_envs = envs()

# get index name
_config_index_name = _envs.get("CONFIG_INDEX_NAME")
if _envs.get("CONFIG_INDEX_NAME") is None:
    _config_index_name = "configs"

# set _config_mappings_path via "CONFIG_MAPPINGS_PATH"
_config_mappings_path = _envs.get("CONFIG_MAPPINGS_PATH")
if _envs.get("CONFIG_MAPPINGS_PATH") is None:
    _config_mappings_path = os.path.realpath(
        f"{dirname(__file__)}/../mappings/{_config_index_name}.json")

# load mappings json
_config_mappings = None
if os.path.isfile(_config_mappings_path):
    with open(_config_mappings_path) as f:
        _config_mappings = json.load(f)


class Configly(Singleton):

    @inspect(_config_index_name, mappings=_config_mappings)
    def __init__(self):
        """
        initialize

        """

    @inspect(_config_index_name, mappings=_config_mappings)
    def _get(self, name):
        """
        get values

        """

        # TODO: mapping確認、なければraise

        # raise AttributeError

        return self

    @inspect(_config_index_name, mappings=_config_mappings)
    def _set(self, key, value):
        """
        set values

        """

    def __getattr__(self, name):
        """
        get values

        :param name:
        :return:
        """
        return self._get(name)

    def __setattr__(self, key, value):
        """
        set values

        :param key:
        :param value:
        :return:
        """

        print(f"[{key}]")
        print(value)

# EOF
