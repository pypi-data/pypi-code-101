from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 61 total commands, 15 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def cbSubset(self):
		"""cbSubset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbSubset'):
			from .CbSubset import CbSubset
			self._cbSubset = CbSubset(self._core, self._cmd_group)
		return self._cbSubset

	@property
	def dmta(self):
		"""dmta commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmta'):
			from .Dmta import Dmta
			self._dmta = Dmta(self._core, self._cmd_group)
		return self._dmta

	@property
	def dmtb(self):
		"""dmtb commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmtb'):
			from .Dmtb import Dmtb
			self._dmtb = Dmtb(self._core, self._cmd_group)
		return self._dmtb

	@property
	def dsid(self):
		"""dsid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsid'):
			from .Dsid import Dsid
			self._dsid = Dsid(self._core, self._cmd_group)
		return self._dsid

	@property
	def fhOffsets(self):
		"""fhOffsets commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhOffsets'):
			from .FhOffsets import FhOffsets
			self._fhOffsets = FhOffsets(self._core, self._cmd_group)
		return self._fhOffsets

	@property
	def fhop(self):
		"""fhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhop'):
			from .Fhop import Fhop
			self._fhop = Fhop(self._core, self._cmd_group)
		return self._fhop

	@property
	def mcbGroups(self):
		"""mcbGroups commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcbGroups'):
			from .McbGroups import McbGroups
			self._mcbGroups = McbGroups(self._core, self._cmd_group)
		return self._mcbGroups

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTable
			self._mcsTable = McsTable(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def mrank(self):
		"""mrank commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mrank'):
			from .Mrank import Mrank
			self._mrank = Mrank(self._core, self._cmd_group)
		return self._mrank

	@property
	def mttPrecoding(self):
		"""mttPrecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mttPrecoding'):
			from .MttPrecoding import MttPrecoding
			self._mttPrecoding = MttPrecoding(self._core, self._cmd_group)
		return self._mttPrecoding

	@property
	def rbgSize(self):
		"""rbgSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbgSize'):
			from .RbgSize import RbgSize
			self._rbgSize = RbgSize(self._core, self._cmd_group)
		return self._rbgSize

	@property
	def resAlloc(self):
		"""resAlloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resAlloc'):
			from .ResAlloc import ResAlloc
			self._resAlloc = ResAlloc(self._core, self._cmd_group)
		return self._resAlloc

	@property
	def scrambling(self):
		"""scrambling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import Scrambling
			self._scrambling = Scrambling(self._core, self._cmd_group)
		return self._scrambling

	@property
	def tpState(self):
		"""tpState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpState'):
			from .TpState import TpState
			self._tpState = TpState(self._core, self._cmd_group)
		return self._tpState

	@property
	def txConfig(self):
		"""txConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txConfig'):
			from .TxConfig import TxConfig
			self._txConfig = TxConfig(self._core, self._cmd_group)
		return self._txConfig

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
