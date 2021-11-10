from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 9 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def tin(self):
		"""tin commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tin'):
			from .Tin import Tin
			self._tin = Tin(self._core, self._cmd_group)
		return self._tin

	@property
	def bitErrorRate(self):
		"""bitErrorRate commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_bitErrorRate'):
			from .BitErrorRate import BitErrorRate
			self._bitErrorRate = BitErrorRate(self._core, self._cmd_group)
		return self._bitErrorRate

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	def get_scount(self) -> int:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:SCOunt \n
		Snippet: value: int = driver.configure.afRf.measurement.data.get_scount() \n
		Sets the number of measurement intervals per measurement cycle. \n
			:return: statistic_count: Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:SCOunt \n
		Snippet: driver.configure.afRf.measurement.data.set_scount(statistic_count = 1) \n
		Sets the number of measurement intervals per measurement cycle. \n
			:param statistic_count: Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:SCOunt {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
