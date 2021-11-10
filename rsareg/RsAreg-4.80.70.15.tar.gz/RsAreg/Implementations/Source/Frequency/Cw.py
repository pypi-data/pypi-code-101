from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cw:
	"""Cw commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cw", core, parent)

	# noinspection PyTypeChecker
	def get_recall(self) -> enums.InclExcl:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:RCL \n
		Snippet: value: enums.InclExcl = driver.source.frequency.cw.get_recall() \n
		Set whether the RF frequency value is retained or taken from a loaded instrument configuration, when you recall
		instrument settings with command *RCL. \n
			:return: rcl: INCLude| EXCLude INCLude Takes the frequency value of the loaded settings. EXCLude Retains the current frequency when an instrument configuration is loaded.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW:RCL?')
		return Conversions.str_to_scalar_enum(response, enums.InclExcl)

	def set_recall(self, rcl: enums.InclExcl) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:RCL \n
		Snippet: driver.source.frequency.cw.set_recall(rcl = enums.InclExcl.EXCLude) \n
		Set whether the RF frequency value is retained or taken from a loaded instrument configuration, when you recall
		instrument settings with command *RCL. \n
			:param rcl: INCLude| EXCLude INCLude Takes the frequency value of the loaded settings. EXCLude Retains the current frequency when an instrument configuration is loaded.
		"""
		param = Conversions.enum_scalar_to_str(rcl, enums.InclExcl)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW:RCL {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW] \n
		Snippet: value: float = driver.source.frequency.cw.get_value() \n
		R&S AREG-B124/-B177: queries the center frequency. R&S AREG-B181: sets the center frequency of the RF output signal. \n
			:return: frequency: float Range: R&S AREG-B124: 24 GHz, R&S AREG-B177: 77 GHz, R&S AREG-B181: 78 GHz and 79 GHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW] \n
		Snippet: driver.source.frequency.cw.set_value(frequency = 1.0) \n
		R&S AREG-B124/-B177: queries the center frequency. R&S AREG-B181: sets the center frequency of the RF output signal. \n
			:param frequency: float Range: R&S AREG-B124: 24 GHz, R&S AREG-B177: 77 GHz, R&S AREG-B181: 78 GHz and 79 GHz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW {param}')
