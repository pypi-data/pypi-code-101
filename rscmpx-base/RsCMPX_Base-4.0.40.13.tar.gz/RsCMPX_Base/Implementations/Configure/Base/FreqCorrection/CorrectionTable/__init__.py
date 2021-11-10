from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 10 total commands, 8 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correctionTable", core, parent)

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	@property
	def erase(self):
		"""erase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_erase'):
			from .Erase import Erase
			self._erase = Erase(self._core, self._cmd_group)
		return self._erase

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .Details import Details
			self._details = Details(self._core, self._cmd_group)
		return self._details

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def exist(self):
		"""exist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exist'):
			from .Exist import Exist
			self._exist = Exist(self._core, self._cmd_group)
		return self._exist

	def delete(self, table_name: str) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DELete \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.delete(table_name = '1') \n
		No command help available \n
			:param table_name: No help available
		"""
		param = Conversions.value_to_quoted_str(table_name)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:DELete {param}')

	def delete_all(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DELete:ALL \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.delete_all(table_path = r1) \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:DELete:ALL {param}'.strip())

	def clone(self) -> 'CorrectionTable':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionTable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
