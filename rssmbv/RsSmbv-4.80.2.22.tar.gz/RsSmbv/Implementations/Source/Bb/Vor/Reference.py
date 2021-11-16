from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def get_deviation(self) -> int:
		"""SCPI: [SOURce<HW>]:[BB]:VOR:REFerence:[DEViation] \n
		Snippet: value: int = driver.source.bb.vor.reference.get_deviation() \n
		Sets the frequency deviation of the reference signal on the FM carrier. \n
			:return: deviation: integer Range: 0 to 960, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:VOR:REFerence:DEViation?')
		return Conversions.str_to_int(response)

	def set_deviation(self, deviation: int) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:VOR:REFerence:[DEViation] \n
		Snippet: driver.source.bb.vor.reference.set_deviation(deviation = 1) \n
		Sets the frequency deviation of the reference signal on the FM carrier. \n
			:param deviation: integer Range: 0 to 960, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:VOR:REFerence:DEViation {param}')
