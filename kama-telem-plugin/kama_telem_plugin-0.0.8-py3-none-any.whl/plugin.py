import os
from typing import List, Dict

from kama_sdk.core.core.plugin_type_defs import PluginManifest
from kama_sdk.utils.descriptor_utils import load_dir_yamls
from kama_telem_plugin.consts import PROTOTYPE_MODE_KTEA
from kama_telem_plugin.models.telem_state_helper import TelemStateHelper


def get_manifest() -> PluginManifest:
  return PluginManifest(
    id='nmachine.telem',
    publisher_identifier='nmachine',
    app_identifier='telem-plugin',
    model_descriptors=gather_model_descriptors(),
    asset_paths=[assets_path],
    model_classes=gather_custom_models(),
    virtual_kteas=[],
    prototype_mode_ktea=PROTOTYPE_MODE_KTEA
  )


def gather_custom_models():
  return [
    TelemStateHelper
  ]


def gather_model_descriptors() -> List[Dict]:
  return load_dir_yamls(descriptors_path, recursive=True)


root_dir = os.path.dirname(os.path.abspath(__file__))
descriptors_path = f'{root_dir}/descriptors'
assets_path = f'{root_dir}/assets'
