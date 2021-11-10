from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ota:
	"""Ota commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ota", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:OTA:OFFSet \n
		Snippet: value: float = driver.source.areGenerator.radar.ota.get_offset() \n
		Defines the distance (air gap) from the R&S AREG100A to the RUT (radar under test) . \n
			:return: areg_ota_offset: float Range: 0.01 to 10, Unit: m
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:OTA:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, areg_ota_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:OTA:OFFSet \n
		Snippet: driver.source.areGenerator.radar.ota.set_offset(areg_ota_offset = 1.0) \n
		Defines the distance (air gap) from the R&S AREG100A to the RUT (radar under test) . \n
			:param areg_ota_offset: float Range: 0.01 to 10, Unit: m
		"""
		param = Conversions.decimal_value_to_str(areg_ota_offset)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:OTA:OFFSet {param}')
