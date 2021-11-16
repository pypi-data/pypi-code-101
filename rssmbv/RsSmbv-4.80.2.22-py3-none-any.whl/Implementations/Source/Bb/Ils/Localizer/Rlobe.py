from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlobe:
	"""Rlobe commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlobe", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:RLOBe:[FREQuency] \n
		Snippet: value: float = driver.source.bb.ils.localizer.rlobe.get_frequency() \n
		Sets the modulation frequency of the antenna lobe arranged at the right viewed from the air plane for the ILS localizer
		modulation signal. \n
			:return: frequency: float Range: 100 to 200
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:LOCalizer:RLOBe:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:RLOBe:[FREQuency] \n
		Snippet: driver.source.bb.ils.localizer.rlobe.set_frequency(frequency = 1.0) \n
		Sets the modulation frequency of the antenna lobe arranged at the right viewed from the air plane for the ILS localizer
		modulation signal. \n
			:param frequency: float Range: 100 to 200
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:LOCalizer:RLOBe:FREQuency {param}')
