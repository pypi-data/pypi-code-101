from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Samples:
	"""Samples commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("samples", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	def get_value(self) -> float:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:SAMPles \n
		Snippet: value: float = driver.source.xrt.generator.arb.samples.get_value() \n
		No command help available \n
			:return: samples: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:SAMPles?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Samples':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Samples(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
