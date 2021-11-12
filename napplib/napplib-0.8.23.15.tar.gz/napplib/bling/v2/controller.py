import requests
from datetime import datetime
from typing import Union, Tuple
from dataclasses import dataclass
from .utils import parse_date_filter

from napplib.utils import AttemptRequests
from napplib.utils	import LoggerSettings

@dataclass
class BlingController():
	debug: bool = False

	def __init__(self, key):
		level = 'INFO' if not self.debug else 'DEBUG'
		LoggerSettings(level=level)

		self.params = dict()
		self.params['apikey'] = key
	
	@AttemptRequests(success_codes=[200])
	def get_products(self, endpoint_base: str,
						   page: str, 
						   with_stock: bool = False,
						   with_images: bool = False,
						   store_code: str = None,
						   inclusion_date: Union[str, datetime, Tuple[str, str], Tuple[datetime, datetime]] = None, 
						   change_date: Union[str, datetime, Tuple[str, str], Tuple[datetime, datetime]] = None):
		headers = {
			'Content-Type'   : 'application/json',
			'Accept-Charset' : 'utf-8',
		}					

		if not page or page < 0:
			raise ValueError('"page" must be greater than 0')
		
		if with_stock:
			self.params['estoque'] = 'S'

		if with_images:
			self.params['imagem'] = 'S'

		if store_code:
			self.params['loja'] = store_code

		filters = []

		if inclusion_date:
			filters.append(parse_date_filter('dataInclusao', inclusion_date))

		if change_date:
			filters.append(parse_date_filter('dataAlteracao', change_date))

		if filters:
			self.params['filters'] = ';'.join(filters)


		return requests.get(f'{endpoint_base}/page={page}/json/', headers=headers, params=self.params)
