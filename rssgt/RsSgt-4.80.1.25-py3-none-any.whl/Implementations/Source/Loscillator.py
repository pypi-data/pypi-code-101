from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loscillator:
	"""Loscillator commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loscillator", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SourceInt:
		"""SCPI: [SOURce<HW>]:LOSCillator:SOURce \n
		Snippet: value: enums.SourceInt = driver.source.loscillator.get_source() \n
		Selects the source of the local oscillator signal. \n
			:return: source: INTernal| EXTernal INT: use built in oscillator; EXT: use signal at [LO/ REF IN] connector
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LOSCillator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_source(self, source: enums.SourceInt) -> None:
		"""SCPI: [SOURce<HW>]:LOSCillator:SOURce \n
		Snippet: driver.source.loscillator.set_source(source = enums.SourceInt.EXTernal) \n
		Selects the source of the local oscillator signal. \n
			:param source: INTernal| EXTernal INT: use built in oscillator; EXT: use signal at [LO/ REF IN] connector
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce<HwInstance>:LOSCillator:SOURce {param}')
