import requests

from dataclasses import dataclass
from typing import  Union
from datetime import datetime
from loguru 	import logger
from napplib.utils	import LoggerSettings

from napplib.utils import AttemptRequests
from .models.product import NuvemshopProductPublished

@logger.catch()
@dataclass
class NuvemShopController():

	store_id : str = None
	token : str = None
	debug : bool = False

	def __post_init__(self):
		level = 'INFO' if not self.debug else 'DEBUG'
		LoggerSettings(level=level)

		self.endpoint_base = f'https://api.nuvemshop.com.br/v1/{self.store_id}'
		self.headers = {}
		self.headers['Authorization'] = f'bearer {self.token}'

	@AttemptRequests(success_codes=[200])
	def get_all_products(self, page: int, limit: int = 100, updated_at_max: Union[str, datetime] = None, published: NuvemshopProductPublished = None):
		params = dict()

		if published:
			params['published'] = published.value

		if updated_at_max:
			params['updated_at_max'] = updated_at_max

		request_headers = self.headers.copy()
		request_headers['Content-Type'] = 'application/json'

		return requests.get(f'{self.endpoint_base}/products?page={page}&per_page={limit}', headers=request_headers, params=params)

