from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CumulativeDistribFnc:
	"""CumulativeDistribFnc commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cumulativeDistribFnc", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def sample(self):
		"""sample commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sample'):
			from .Sample import Sample
			self._sample = Sample(self._core, self._cmd_group)
		return self._sample

	@property
	def probability(self):
		"""probability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_probability'):
			from .Probability import Probability
			self._probability = Probability(self._core, self._cmd_group)
		return self._probability

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF \n
		Snippet: value: List[float] = driver.gprf.measurement.power.cumulativeDistribFnc.fetch() \n
		Returns the CCDF diagram contents. \n
		Suppressed linked return values: reliability \n
			:return: results: 4096 results, each representing a 0.047-dB interval ('bin')"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF?', suppressed)
		return response

	def clone(self) -> 'CumulativeDistribFnc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CumulativeDistribFnc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
