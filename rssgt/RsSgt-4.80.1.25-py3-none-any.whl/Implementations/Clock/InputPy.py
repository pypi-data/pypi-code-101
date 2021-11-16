from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: CLOCk:INPut:FREQuency \n
		Snippet: value: float = driver.clock.inputPy.get_frequency() \n
		Queries the measured frequency of the external clock signal. An external clock reference must be supplied at the
		[USER1/2] input. \n
			:return: frequency: float Range: 0 to max
		"""
		response = self._core.io.query_str('CLOCk:INPut:FREQuency?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SlopeType:
		"""SCPI: CLOCk:INPut:SLOPe \n
		Snippet: value: enums.SlopeType = driver.clock.inputPy.get_slope() \n
		The command sets the active slope of an externally applied clock signal at the [USER 1/2] connector. \n
			:return: slope: NEGative| POSitive
		"""
		response = self._core.io.query_str('CLOCk:INPut:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_slope(self, slope: enums.SlopeType) -> None:
		"""SCPI: CLOCk:INPut:SLOPe \n
		Snippet: driver.clock.inputPy.set_slope(slope = enums.SlopeType.NEGative) \n
		The command sets the active slope of an externally applied clock signal at the [USER 1/2] connector. \n
			:param slope: NEGative| POSitive
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		self._core.io.write(f'CLOCk:INPut:SLOPe {param}')
