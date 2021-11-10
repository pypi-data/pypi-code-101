from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtFive:
	"""PtFive commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptFive", core, parent)

	def get_symbol_rate(self) -> int:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:PTFive:SRATe \n
		Snippet: value: int = driver.configure.vse.measurement.ptFive.get_symbol_rate() \n
		No command help available \n
			:return: symbol_rate: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:PTFive:SRATe?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.P25Mode:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:PTFive:MODE \n
		Snippet: value: enums.P25Mode = driver.configure.vse.measurement.ptFive.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:PTFive:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.P25Mode)

	# noinspection PyTypeChecker
	def get_filter_py(self) -> enums.PulseShapingUserFilter:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:PTFive:FILTer \n
		Snippet: value: enums.PulseShapingUserFilter = driver.configure.vse.measurement.ptFive.get_filter_py() \n
		No command help available \n
			:return: filter_py: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:PTFive:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.PulseShapingUserFilter)
