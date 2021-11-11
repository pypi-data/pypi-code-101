import json

from abc import ABC, abstractmethod
from flask import send_file

class NaogiModel(ABC):
  def __init__(self, renderer=JsonRenderer):
    super()
    self.model = None

  @abstractmethod
  def predict(self):
    pass

  @abstractmethod
  def load_model(self):
    pass

  @abstractmethod
  def prepare(self):
    pass

  def renderer(self):
    return JsonRenderer

class AbstractRenderer(ABC):
  @abstractmethod
  def render(data):
    pass

class JsonRenderer(AbstractRenderer):
  def render(data):
    return json.dumps(data)

class FileRenderer(AbstractRenderer):
  def render(binary, filename='file', content_type=None, downloadable=False):
    return send_file(
      binary,
      mimetype=content_type,
      as_attachment=downloadable,
      download_name=filename,
    )
