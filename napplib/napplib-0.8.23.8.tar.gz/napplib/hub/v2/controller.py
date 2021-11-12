# build-in imports
from dataclasses 	import dataclass
from typing 		import List
from typing 		import Optional

# external imports
import requests
from loguru import logger

# project imports
from .models.catalog	import HubSku
from .models.catalog	import HubSkuPrice
from .models.catalog	import HubSkuStock
from .models.order	    import HubOrder
from .models.channel	import ChannelType
from .models.channel	import ChannelStatus
from .utils				import Environment
from napplib.utils		import AttemptRequests
from napplib.utils		import unpack_payload_dict
from napplib.utils		import LoggerSettings


@dataclass
class HubController:
	"""[This controller has the function to execute the calls inside the Napp HUB V2.
		All functions will return a requests.Response.]

	Args:
		environment	(Environment): [The environment for making requests.].
		token 		(str): [The Authorization Token.].
		debug 		(bool, optional): [Parameter to set the display of DEBUG logs.]. Defaults to False.

	Raises:
		TypeError: [If the environment is not valid, it will raise a TypeError.]
		TypeError: [If the token is not valid, it will raise a TypeError.]
		ValueError: [If the token is empty or None, it will raise a ValueError.]
	"""

	def __init__(self,
		environment				: Environment,
		token					: str = None,
		debug					: bool = False,
		endpoint_development	: Optional[str] = None):
		
		self.environment = environment
		self.token = token
		self.debug = debug
		self.endpoint_development = endpoint_development

		level = 'INFO' if not self.debug else 'DEBUG'
		LoggerSettings(level=level)

		if not isinstance(self.environment, Environment):
			raise TypeError(f'please enter a valid environment. environment: {self.environment}')

		if not isinstance(self.token, str):
			raise TypeError(f'please enter a valid token. token: {self.token}')

		if not self.token:
			raise ValueError(f'Please provide a token.')

		self.headers = {
			'Authorization': f'Bearer {self.token}'
		}

	@AttemptRequests(success_codes=[200])
	def get_sku_by_id(self, sku_id: str):
		return requests.get(f'{self.__get_endpoint_base()}/skus/{sku_id}', headers=self.headers)

	@AttemptRequests(success_codes=[200])
	def get_price_and_stock_by_external_ids(self, external_seller_id: str, external_channel_id: str, external_sku: str):
		return requests.get(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/channels/{external_channel_id}/skus/external/{external_sku}', headers=self.headers)

	@AttemptRequests(success_codes=[200])
	def put_order(self, external_seller_id: str, external_channel_id: str, order: HubOrder):
		return requests.put(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/channels/{external_channel_id}/orders', headers=self.headers, data=unpack_payload_dict(order,remove_null=True))

	@AttemptRequests(success_codes=[200])
	def get_order_by_id(self, order_id: str):
		return requests.get(f'{self.__get_endpoint_base()}/orders/{order_id}', headers=self.headers)

	@AttemptRequests(success_codes=[200])
	def get_logistics_shipping_fee(self, external_seller_id: str, zip_code: str):
		return requests.get(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/logistics/zipcode/{zip_code}/shipping/fee', headers=self.headers)

	@AttemptRequests(success_codes=[200])
	def get_seller_channel_type(self, external_seller_id: str, external_channel_id: str, channel_type: ChannelType):
		return requests.get(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/channels/{external_channel_id}/type/{channel_type.value}', headers=self.headers)

	@AttemptRequests(success_codes=[204])
	def put_channel_sku_status(self, channel_sku_id: str, channel_status: ChannelStatus):
		return requests.put(f'{self.__get_endpoint_base()}/channels/skus/{channel_sku_id}/status', headers=self.headers, data=unpack_payload_dict(channel_status,remove_null=True))

	@AttemptRequests(success_codes=[200])
	def put_skus(self, skus: List[HubSku], external_seller_id: int):
		return requests.put(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/skus', headers=self.headers, data=unpack_payload_dict(skus,remove_null=True))

	@AttemptRequests(success_codes=[200])
	def put_skus_prices(self, external_seller_id: str, skus_prices: List[HubSkuPrice]):
		return requests.put(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/skus/prices', headers=self.headers, data=unpack_payload_dict(skus_prices,remove_null=True))
	
	@AttemptRequests(success_codes=[200])
	def put_skus_stocks(self, external_seller_id: str, skus_stocks: List[HubSkuStock]):
		return requests.put(f'{self.__get_endpoint_base()}/sellers/{external_seller_id}/skus/stocks', headers=self.headers, data=unpack_payload_dict(skus_stocks,remove_null=True))

	def __get_endpoint_base(self): 
		if self.environment == Environment.DEVELOPMENT and self.endpoint_development:
			return self.endpoint_development

		return self.environment.value