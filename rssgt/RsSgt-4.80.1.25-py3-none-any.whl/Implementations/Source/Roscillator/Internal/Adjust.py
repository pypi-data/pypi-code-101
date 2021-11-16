from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adjust:
	"""Adjust commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adjust", core, parent)

	def get_value(self) -> int:
		"""SCPI: [SOURce]:ROSCillator:[INTernal]:ADJust:VALue \n
		Snippet: value: int = driver.source.roscillator.internal.adjust.get_value() \n
		Allows an application to shift the reference oscillator frequency by a small amount. The setting range depends on the
		reference oscillator type and its factory calibration value. Allowed are the following ranges:
			INTRO_CMD_HELP: Not affected are: \n
			- For TCXO oscillator: Max - Min = 1023
			- For OCXO oscillator: Max - Min = 65535 (option R&S SGT-B1 required.)  \n
			:return: value: integer Range: Min to Max
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:INTernal:ADJust:VALue?')
		return Conversions.str_to_int(response)

	def set_value(self, value: int) -> None:
		"""SCPI: [SOURce]:ROSCillator:[INTernal]:ADJust:VALue \n
		Snippet: driver.source.roscillator.internal.adjust.set_value(value = 1) \n
		Allows an application to shift the reference oscillator frequency by a small amount. The setting range depends on the
		reference oscillator type and its factory calibration value. Allowed are the following ranges:
			INTRO_CMD_HELP: Not affected are: \n
			- For TCXO oscillator: Max - Min = 1023
			- For OCXO oscillator: Max - Min = 65535 (option R&S SGT-B1 required.)  \n
			:param value: integer Range: Min to Max
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SOURce:ROSCillator:INTernal:ADJust:VALue {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:ROSCillator:[INTernal]:ADJust:[STATe] \n
		Snippet: value: bool = driver.source.roscillator.internal.adjust.get_state() \n
		Determines whether the calibrated (OFF) or a user-defined (ON) adjustment value is used for fine adjustment of the
		frequency. If user-defined values are used, the instrument is no longer in the calibrated state. However, the calibration
		value is not changed and the instrument resumes the calibrated state after sending the command
		SOURce:ROSCillator:INTernal:ADJust:STATe OFF. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:INTernal:ADJust:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:ROSCillator:[INTernal]:ADJust:[STATe] \n
		Snippet: driver.source.roscillator.internal.adjust.set_state(state = False) \n
		Determines whether the calibrated (OFF) or a user-defined (ON) adjustment value is used for fine adjustment of the
		frequency. If user-defined values are used, the instrument is no longer in the calibrated state. However, the calibration
		value is not changed and the instrument resumes the calibrated state after sending the command
		SOURce:ROSCillator:INTernal:ADJust:STATe OFF. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:ROSCillator:INTernal:ADJust:STATe {param}')
