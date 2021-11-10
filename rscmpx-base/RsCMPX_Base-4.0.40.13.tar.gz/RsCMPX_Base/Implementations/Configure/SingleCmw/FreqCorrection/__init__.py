from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqCorrection:
	"""FreqCorrection commands group definition. 8 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqCorrection", core, parent)

	@property
	def activate(self):
		"""activate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_activate'):
			from .Activate import Activate
			self._activate = Activate(self._core, self._cmd_group)
		return self._activate

	@property
	def deactivate(self):
		"""deactivate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_deactivate'):
			from .Deactivate import Deactivate
			self._deactivate = Deactivate(self._core, self._cmd_group)
		return self._deactivate

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import Usage
			self._usage = Usage(self._core, self._cmd_group)
		return self._usage

	def deactivate_all(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:CMWS:FDCorrection:DEACtivate:ALL \n
		Snippet: driver.configure.singleCmw.freqCorrection.deactivate_all(table_path = r1) \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:CMWS:FDCorrection:DEACtivate:ALL {param}'.strip())

	def clone(self) -> 'FreqCorrection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqCorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
