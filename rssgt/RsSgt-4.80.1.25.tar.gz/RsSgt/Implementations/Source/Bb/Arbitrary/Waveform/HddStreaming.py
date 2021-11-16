from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HddStreaming:
	"""HddStreaming commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hddStreaming", core, parent)

	def get_blevel(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:BLEVel \n
		Snippet: value: int = driver.source.bb.arbitrary.waveform.hddStreaming.get_blevel() \n
		Queries the filling level of the streaming buffer. \n
			:return: blevel: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:BLEVel?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:STATe \n
		Snippet: value: bool = driver.source.bb.arbitrary.waveform.hddStreaming.get_state() \n
		Enables/disables the streaming of modulation data directly from the hard drive (HDD) . HDD streaming is recommended for
		processing of large files that require more ARB memory than the currently installed one. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:STATe \n
		Snippet: driver.source.bb.arbitrary.waveform.hddStreaming.set_state(state = False) \n
		Enables/disables the streaming of modulation data directly from the hard drive (HDD) . HDD streaming is recommended for
		processing of large files that require more ARB memory than the currently installed one. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:STATe {param}')
