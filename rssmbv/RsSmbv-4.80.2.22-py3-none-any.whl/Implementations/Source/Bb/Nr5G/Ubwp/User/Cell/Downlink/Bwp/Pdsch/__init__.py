from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 47 total commands, 14 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	@property
	def cbgf(self):
		"""cbgf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbgf'):
			from .Cbgf import Cbgf
			self._cbgf = Cbgf(self._core, self._cmd_group)
		return self._cbgf

	@property
	def dmta(self):
		"""dmta commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmta'):
			from .Dmta import Dmta
			self._dmta = Dmta(self._core, self._cmd_group)
		return self._dmta

	@property
	def dmtb(self):
		"""dmtb commands group. 6 Sub-classes, 0 commands."""
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
	def mcwdci(self):
		"""mcwdci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcwdci'):
			from .Mcwdci import Mcwdci
			self._mcwdci = Mcwdci(self._core, self._cmd_group)
		return self._mcwdci

	@property
	def prec(self):
		"""prec commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_prec'):
			from .Prec import Prec
			self._prec = Prec(self._core, self._cmd_group)
		return self._prec

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
	def td(self):
		"""td commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_td'):
			from .Td import Td
			self._td = Td(self._core, self._cmd_group)
		return self._td

	@property
	def tdaNum(self):
		"""tdaNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdaNum'):
			from .TdaNum import TdaNum
			self._tdaNum = TdaNum(self._core, self._cmd_group)
		return self._tdaNum

	@property
	def vpInter(self):
		"""vpInter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vpInter'):
			from .VpInter import VpInter
			self._vpInter = VpInter(self._core, self._cmd_group)
		return self._vpInter

	def clone(self) -> 'Pdsch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
