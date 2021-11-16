from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimization:
	"""Optimization commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimization", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BbImpOptMode:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:MODE \n
		Snippet: value: enums.BbImpOptMode = driver.source.bb.impairment.optimization.get_mode() \n
		This command sets the optimization mode. \n
			:return: mode: FAST| QHIGh FAST Optimization is reached by compensation for I/Q skew. QHIGh Optimization is reached by compensation for I/Q skew and frequency response correction.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IMPairment:OPTimization:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BbImpOptMode)

	def set_mode(self, mode: enums.BbImpOptMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:MODE \n
		Snippet: driver.source.bb.impairment.optimization.set_mode(mode = enums.BbImpOptMode.FAST) \n
		This command sets the optimization mode. \n
			:param mode: FAST| QHIGh FAST Optimization is reached by compensation for I/Q skew. QHIGh Optimization is reached by compensation for I/Q skew and frequency response correction.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BbImpOptMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:IMPairment:OPTimization:MODE {param}')
