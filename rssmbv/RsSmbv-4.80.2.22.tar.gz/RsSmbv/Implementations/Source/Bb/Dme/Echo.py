from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Echo:
	"""Echo commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("echo", core, parent)

	def get_attenuation(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO:ATTenuation \n
		Snippet: value: float = driver.source.bb.dme.echo.get_attenuation() \n
		Sets the attenuation of the DME echo pulse pair signal compared to the original DME pulse pair signal. \n
			:return: echo_atten: float Range: 0 to 50, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DME:ECHO:ATTenuation?')
		return Conversions.str_to_float(response)

	def set_attenuation(self, echo_atten: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO:ATTenuation \n
		Snippet: driver.source.bb.dme.echo.set_attenuation(echo_atten = 1.0) \n
		Sets the attenuation of the DME echo pulse pair signal compared to the original DME pulse pair signal. \n
			:param echo_atten: float Range: 0 to 50, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(echo_atten)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:ECHO:ATTenuation {param}')

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO:DELay \n
		Snippet: value: float = driver.source.bb.dme.echo.get_delay() \n
		Sets the delay between the first original DME pulse pair signal and second DME echo pulse pair signal. \n
			:return: echo_del: float Range: 15.5E-6 to 204E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DME:ECHO:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, echo_del: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO:DELay \n
		Snippet: driver.source.bb.dme.echo.set_delay(echo_del = 1.0) \n
		Sets the delay between the first original DME pulse pair signal and second DME echo pulse pair signal. \n
			:param echo_del: float Range: 15.5E-6 to 204E-6
		"""
		param = Conversions.decimal_value_to_str(echo_del)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:ECHO:DELay {param}')

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO \n
		Snippet: value: bool = driver.source.bb.dme.echo.get_value() \n
		Enables the simulation of DME echo pulse pair signals. \n
			:return: extendet_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DME:ECHO?')
		return Conversions.str_to_bool(response)

	def set_value(self, extendet_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:DME:ECHO \n
		Snippet: driver.source.bb.dme.echo.set_value(extendet_state = False) \n
		Enables the simulation of DME echo pulse pair signals. \n
			:param extendet_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(extendet_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:ECHO {param}')
