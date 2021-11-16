from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def fetch(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:TRACe:GAIN \n
		Snippet: value: List[float] = driver.gprf.measurement.ploss.eval.trace.gain.fetch(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param connector: No help available
			:param path_index: No help available
			:return: gain: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum, enums.CmwsConnector), ArgSingle('path_index', path_index, DataType.Enum, enums.PathIndex, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:TRACe:GAIN? {param}'.rstrip(), suppressed)
		return response
