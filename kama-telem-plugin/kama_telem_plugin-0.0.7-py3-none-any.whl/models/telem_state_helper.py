from typing import Optional

from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.telem.telem_manager import telem_manager
from kama_sdk.model.base.model import Model
from kama_sdk.model.base.model_decorators import model_attr
from kama_telem_plugin.nmachine_telem_backend import NMachineTelemBackend


class TelemStateHelper(Model):

  @model_attr(key='is_online', cached=True)
  def is_online(self) -> bool:
    if backend := get_backend():
      return backend.is_enabled() and backend.is_online()
    else:
      return False

  @model_attr(key='is_offline', cached=True)
  def is_offline(self):
    return not self.is_online()

  @model_attr(key='is_enabled', cached=True)
  def is_enabled(self):
    if backend := get_backend():
      return backend.is_enabled() and backend.is_enabled()
    else:
      return False

  @model_attr(key='is_disabled', cached=True)
  def is_disabled(self):
    return not self.is_enabled()

  @model_attr(key='svc', cached=True)
  def get_svc(self) -> Optional[KatSvc]:
    if backend := get_backend():
      return backend.get_svc()

  @model_attr(key='strategy')
  def get_strategy(self) -> Optional[str]:
    if backend := get_backend():
      return backend.get_strategy()

  @model_attr(key='status', cached=True)
  def status(self):
    if backend := get_backend():
      if backend.is_enabled():
        if backend.is_online():
          return 'online'
        else:
          return 'offline'
      else:
        return 'disabled'
    else:
      return 'disabled'


def get_backend() -> Optional[NMachineTelemBackend]:
  backend = telem_manager.get_backend()
  is_from_this_plugin = isinstance(backend, NMachineTelemBackend)
  return backend if is_from_this_plugin else None
