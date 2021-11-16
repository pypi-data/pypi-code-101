from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bband:
	"""Bband commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bband", core, parent)

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SlopeType:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:[BBANd]:SLOPe \n
		Snippet: value: enums.SlopeType = driver.source.inputPy.trigger.bband.get_slope() \n
		No command help available \n
			:return: slope: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TRIGger:BBANd:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_slope(self, slope: enums.SlopeType) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:[BBANd]:SLOPe \n
		Snippet: driver.source.inputPy.trigger.bband.set_slope(slope = enums.SlopeType.NEGative) \n
		No command help available \n
			:param slope: No help available
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TRIGger:BBANd:SLOPe {param}')
