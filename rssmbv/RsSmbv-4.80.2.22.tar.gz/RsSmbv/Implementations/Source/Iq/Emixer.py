from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emixer:
	"""Emixer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emixer", core, parent)

	def get_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:EMIXer:MODE \n
		Snippet: value: bool = driver.source.iq.emixer.get_mode() \n
		If enabled, the upper frequency, until a direct I/Q modulation is used, is shifted to 200 MHz. For details, see 'Extended
		Mixer Mode'. \n
			:return: mixer_mode: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:EMIXer:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, mixer_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:EMIXer:MODE \n
		Snippet: driver.source.iq.emixer.set_mode(mixer_mode = False) \n
		If enabled, the upper frequency, until a direct I/Q modulation is used, is shifted to 200 MHz. For details, see 'Extended
		Mixer Mode'. \n
			:param mixer_mode: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(mixer_mode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:EMIXer:MODE {param}')
