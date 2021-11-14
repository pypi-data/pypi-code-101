import requests
from napplib.utils import AttemptRequests

class NuvemShopController: 
	def __init__(self, store_id, token, email,):
		self.token = token
		self.email = email
		self.store_id = store_id

		self.url = f'https://api.nuvemshop.com.br/v1/{store_id}'
		self.limit = 100
		self.headers = {
		'Authentication' : f'bearer {self.token}',
		'Content-Type'   : 'application/json',
		'User-Agent' : f'MyApp {self.email}',
		}

	@AttemptRequests(success_codes=[200])
	def get_products(self, page):
		url_products = f'{self.url}/products?page={page}&per_page={self.limit}'
		return requests.get(url_products, headers=self.headers)

	@AttemptRequests(success_codes=[200])
	def get_category(self, store_id, categ_ig):
		url_categories = f'{self.url}/categories/{categ_ig}'
		return requests.get(url_categories, headers=self.headers)