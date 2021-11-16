import datetime


class NewsObject:
	"""[pyplazmix.NewsObject] - Plazmix News Object

	:param data: NewsObject data
	:type data: dict
	"""
	def __init__(self, data: dict):
		self.id = data['id']
		self.title = data['title']
		self.image = data['image']
		self.author = data['author']
		self.short_text = data['short_text']
		self.full_text = data['full_text']
		self.more_link = data['more_link']
		self.read_time = data['read_time']

	def __repr__(self):
		return f'<NewsObject id={self.id} title="{self.title}">'