from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 5 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import Snumber
			self._snumber = Snumber(self._core, self._cmd_group)
		return self._snumber

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	def get_pn_mode(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:PNMode \n
		Snippet: value: bool = driver.diagnostic.gprf.generator.get_pn_mode() \n
		No command help available \n
			:return: pn_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:GENerator<Instance>:PNMode?')
		return Conversions.str_to_bool(response)

	def set_pn_mode(self, pn_mode: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:PNMode \n
		Snippet: driver.diagnostic.gprf.generator.set_pn_mode(pn_mode = False) \n
		No command help available \n
			:param pn_mode: No help available
		"""
		param = Conversions.bool_to_str(pn_mode)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:PNMode {param}')

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
