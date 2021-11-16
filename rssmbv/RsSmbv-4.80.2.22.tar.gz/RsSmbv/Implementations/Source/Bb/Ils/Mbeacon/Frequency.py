from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AvionicCarrFreqModeMrkBcn:
		"""SCPI: [SOURce<HW>]:[BB]:[ILS]:MBEacon:FREQuency:MODE \n
		Snippet: value: enums.AvionicCarrFreqModeMrkBcn = driver.source.bb.ils.mbeacon.frequency.get_mode() \n
		Sets the mode for the carrier frequency of the signal. \n
			:return: mode: USER| PREDefined
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:MBEacon:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AvionicCarrFreqModeMrkBcn)

	def set_mode(self, mode: enums.AvionicCarrFreqModeMrkBcn) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:[ILS]:MBEacon:FREQuency:MODE \n
		Snippet: driver.source.bb.ils.mbeacon.frequency.set_mode(mode = enums.AvionicCarrFreqModeMrkBcn.PREDefined) \n
		Sets the mode for the carrier frequency of the signal. \n
			:param mode: USER| PREDefined
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AvionicCarrFreqModeMrkBcn)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:MBEacon:FREQuency:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:[ILS]:MBEacon:FREQuency \n
		Snippet: value: float = driver.source.bb.ils.mbeacon.frequency.get_value() \n
		Sets the carrier frequency for the ILS marker beacon signal. \n
			:return: carrier_freq: float Range: 100E3 to 6E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:MBEacon:FREQuency?')
		return Conversions.str_to_float(response)

	def set_value(self, carrier_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:[ILS]:MBEacon:FREQuency \n
		Snippet: driver.source.bb.ils.mbeacon.frequency.set_value(carrier_freq = 1.0) \n
		Sets the carrier frequency for the ILS marker beacon signal. \n
			:param carrier_freq: float Range: 100E3 to 6E9
		"""
		param = Conversions.decimal_value_to_str(carrier_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:MBEacon:FREQuency {param}')
