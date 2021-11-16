from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fall:
	"""Fall commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fall", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:FALL:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.fall.get_time() \n
		No command help available \n
			:return: fall_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:FALL:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, fall_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:FALL:TIME \n
		Snippet: driver.source.bb.pramp.ramp.fall.set_time(fall_time = 1.0) \n
		No command help available \n
			:param fall_time: No help available
		"""
		param = Conversions.decimal_value_to_str(fall_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:FALL:TIME {param}')
