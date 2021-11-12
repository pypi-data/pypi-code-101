import base64
import json
from typing import Dict, List, Optional, Any, Union

import requests
from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.core.config_man import config_man
from kama_sdk.core.telem.telem_backend import TelemBackend
from kama_sdk.utils import env_utils, utils
from kama_telem_plugin.consts import SVC_NAME, PLUGIN_ID, STRATEGY_KEY


class NMachineTelemBackend(TelemBackend):

  def is_enabled(self) -> bool:
    value = config_man.read_var(STRATEGY_KEY, space=PLUGIN_ID)
    return utils.any2bool(value)

  def is_online(self) -> bool:
    return self.collection_names() is not None

  @staticmethod
  def get_strategy() -> str:
    return config_man.read_var(STRATEGY_KEY, space=PLUGIN_ID)

  def collection_names(self) -> List[str]:
    endpoint = f"/collections/index"
    return self.do_get(endpoint, {})

  def drop_collection(self, coll_id: str):
    endpoint = f"/collections/{coll_id}/drop"
    return self.do_post(endpoint, {}, {})

  def create_record(self, coll_id: str, record: Dict):
    endpoint = f"/collections/{coll_id}/insert"
    self.do_post(endpoint, {}, {'data': record})

  def update_record(self, coll_id: str, record: Dict):
    pass

  def find_record_by_id(self, coll_id: str, record_id) -> Optional[Dict]:
    endpoint = f"/collections/{coll_id}/find/{record_id}"
    return self.do_get(endpoint, {})

  def query_collection(self, coll_id: str, query: Dict) -> List[Dict]:
    endpoint = f"/collections/{coll_id}/query"
    args = encode_query_arg(query)
    return self.do_get(endpoint, args)

  @staticmethod
  def get_svc() -> Optional[KatSvc]:
    return KatSvc.find(SVC_NAME, config_man.get_ns())

  @staticmethod
  def do_get(path: str, args: Dict) -> Optional[Union[Dict, List]]:
    if env_utils.is_in_cluster():
      url = path2in_cluster_url(path)
      return requests.get(url).json()
    else:
      if svc := NMachineTelemBackend.get_svc():
        result = svc.proxy_get(path, args)
        return parse_proxy_response(result)
      else:
        return None

  @staticmethod
  def do_post(path: str, args: Dict, bod) -> Optional[Union[Dict, List]]:
    if env_utils.is_in_cluster():
      url = path2in_cluster_url(path)
      return requests.post(url, json=bod).json()
    else:
      if svc := NMachineTelemBackend.get_svc():
        result = svc.proxy_post(path, args, bod)
        # print(result)
        return parse_proxy_response(result)
      else:
        return None


def encode_query_arg(query: Dict) -> Dict:
  if query:
    query_str = json.dumps(query or {})
    b64_enc_query = base64.b64encode(query_str.encode())
    return dict(query=b64_enc_query)
  else:
    return {}


def parse_proxy_response(result: Any) -> Optional[Union[Dict, List]]:
  if isinstance(result, dict):
    if result.get('status') < 400:
      parsed_body = result.get('body')
      if parsed_body and 'data' in parsed_body.keys():
        return parsed_body.get('data')
      else:
        return parsed_body
    else:
      return None


def path2in_cluster_url(path: str) -> str:
  base = f"http://{SVC_NAME}.{config_man.ns()}:5000"
  return f"{base}/{path}"
