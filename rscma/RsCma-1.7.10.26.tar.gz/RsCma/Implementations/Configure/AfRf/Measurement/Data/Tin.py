from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tin:
	"""Tin commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tin", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:ENABle \n
		Snippet: value: bool = driver.configure.afRf.measurement.data.tin.get_enable() \n
		Enables or disables analysis of data from the TTL connector. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:ENABle \n
		Snippet: driver.configure.afRf.measurement.data.tin.set_enable(enable = False) \n
		Enables or disables analysis of data from the TTL connector. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:ENABle {param}')

	# noinspection PyTypeChecker
	def get_data(self) -> enums.ClockIn:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:DATA \n
		Snippet: value: enums.ClockIn = driver.configure.afRf.measurement.data.tin.get_data() \n
		tbd \n
			:return: data: PIN14 | PIN15
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.ClockIn)

	def set_data(self, data: enums.ClockIn) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:DATA \n
		Snippet: driver.configure.afRf.measurement.data.tin.set_data(data = enums.ClockIn.PIN14) \n
		tbd \n
			:param data: PIN14 | PIN15
		"""
		param = Conversions.enum_scalar_to_str(data, enums.ClockIn)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:DATA {param}')

	# noinspection PyTypeChecker
	def get_clock(self) -> enums.ClockIn:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:CLOCk \n
		Snippet: value: enums.ClockIn = driver.configure.afRf.measurement.data.tin.get_clock() \n
		Sets the bit rate that is expected at the TTL interface. \n
			:return: clock: PIN14 | PIN15
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:CLOCk?')
		return Conversions.str_to_scalar_enum(response, enums.ClockIn)

	def set_clock(self, clock: enums.ClockIn) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:CLOCk \n
		Snippet: driver.configure.afRf.measurement.data.tin.set_clock(clock = enums.ClockIn.PIN14) \n
		Sets the bit rate that is expected at the TTL interface. \n
			:param clock: PIN14 | PIN15
		"""
		param = Conversions.enum_scalar_to_str(clock, enums.ClockIn)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:TIN:CLOCk {param}')
