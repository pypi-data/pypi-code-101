from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqCorrection:
	"""FreqCorrection commands group definition. 12 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqCorrection", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 8 Sub-classes, 2 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._cmd_group)
		return self._correctionTable

	def save(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:SAV \n
		Snippet: driver.configure.base.freqCorrection.save(table_path = r1) \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:SAV {param}'.strip())

	def recall(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:RCL \n
		Snippet: driver.configure.base.freqCorrection.recall(table_path = r1) \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:RCL {param}'.strip())

	def clone(self) -> 'FreqCorrection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqCorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
