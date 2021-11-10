from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	def get_attenuation(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:BASE:ATTenuation \n
		Snippet: value: int = driver.source.areGenerator.radar.base.get_attenuation() \n
		Defines the attenuation affecting all radar objects. Together with the individual attenuation for a single radar object,
		it forms the total attenuation for the specific object. \n
			:return: areg_base_att: integer Range: -50 to 150, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:BASE:ATTenuation?')
		return Conversions.str_to_int(response)

	def set_attenuation(self, areg_base_att: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:BASE:ATTenuation \n
		Snippet: driver.source.areGenerator.radar.base.set_attenuation(areg_base_att = 1) \n
		Defines the attenuation affecting all radar objects. Together with the individual attenuation for a single radar object,
		it forms the total attenuation for the specific object. \n
			:param areg_base_att: integer Range: -50 to 150, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(areg_base_att)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:BASE:ATTenuation {param}')
