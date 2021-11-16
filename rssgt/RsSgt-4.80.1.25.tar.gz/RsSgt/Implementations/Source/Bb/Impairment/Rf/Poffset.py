from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, phase_offset: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:POFFset \n
		Snippet: driver.source.bb.impairment.rf.poffset.set(phase_offset = 1.0, path = repcap.Path.Default) \n
		No command help available \n
			:param phase_offset: No help available
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce:BB:IMPairment:RF{path_cmd_val}:POFFset {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:POFFset \n
		Snippet: value: float = driver.source.bb.impairment.rf.poffset.get(path = repcap.Path.Default) \n
		No command help available \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: phase_offset: No help available"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:RF{path_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
