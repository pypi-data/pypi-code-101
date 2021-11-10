from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect:ALL:[STATe] \n
		Snippet: value: bool = driver.source.areGenerator.object.all.get_state() \n
		Switches all available radar objects (1 to 4) on or off simultaneously. \n
			:return: global_obj_stat: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OBJect:ALL:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, global_obj_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect:ALL:[STATe] \n
		Snippet: driver.source.areGenerator.object.all.set_state(global_obj_stat = False) \n
		Switches all available radar objects (1 to 4) on or off simultaneously. \n
			:param global_obj_stat: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(global_obj_stat)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OBJect:ALL:STATe {param}')
