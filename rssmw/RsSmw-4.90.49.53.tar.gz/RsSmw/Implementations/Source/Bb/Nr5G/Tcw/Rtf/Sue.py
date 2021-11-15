from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sue:
	"""Sue commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sue", core, parent)

	def get_bb_selector(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SUE:BBSelector \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.rtf.sue.get_bb_selector() \n
		No command help available \n
			:return: suebb_selector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:SUE:BBSelector?')
		return Conversions.str_to_int(response)

	def set_bb_selector(self, suebb_selector: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SUE:BBSelector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.sue.set_bb_selector(suebb_selector = 1) \n
		No command help available \n
			:param suebb_selector: No help available
		"""
		param = Conversions.decimal_value_to_str(suebb_selector)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:SUE:BBSelector {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SUE:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.nr5G.tcw.rtf.sue.get_connector() \n
		No command help available \n
			:return: sue_connector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:SUE:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)

	def set_connector(self, sue_connector: enums.FeedbackConnector) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SUE:CONNector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.sue.set_connector(sue_connector = enums.FeedbackConnector.GLOBal) \n
		No command help available \n
			:param sue_connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(sue_connector, enums.FeedbackConnector)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:SUE:CONNector {param}')
