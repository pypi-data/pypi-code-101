from datetime import datetime


class OnlineNow:
	"""[pyplazmix.OnlineNow] - Plazmix Online Now

	:param data: Online now object
	:type data: dict
	"""
	def __init__(self, data: dict):
		self.summary = [OnlineObject(x) for x in data['summary']]
		self.modes = [OnlineObject(x) for x in data['modes']]

	def __repr__(self):
		return f"<OnlineNow summary_objects={len(self.summary)} modes_objects={len(self.modes)}>"

class OnlineObject:
	"""[pyplazmix.OnlineObject] - Plazmix Online Object

	:param data: Online object
	:type data: dict
	"""
	def __init__(self, data: dict):
		self.label = data['label']
		self.identification = data['identification']
		self.last_update = datetime.fromtimestamp(int(data['last_update']))
		self.online = data['online']

	def __repr__(self):
		return f'<OnlineObject label="{self.label}" online={self.online}>'