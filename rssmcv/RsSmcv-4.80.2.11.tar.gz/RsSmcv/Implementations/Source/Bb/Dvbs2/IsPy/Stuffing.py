from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stuffing:
	"""Stuffing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stuffing", core, parent)

	def set(self, stuffing: bool, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:STUFfing \n
		Snippet: driver.source.bb.dvbs2.isPy.stuffing.set(stuffing = False, inputStream = repcap.InputStream.Default) \n
		Activates stuffing. \n
			:param stuffing: 0| 1| OFF| ON
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.bool_to_str(stuffing)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:STUFfing {param}')

	def get(self, inputStream=repcap.InputStream.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:STUFfing \n
		Snippet: value: bool = driver.source.bb.dvbs2.isPy.stuffing.get(inputStream = repcap.InputStream.Default) \n
		Activates stuffing. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: stuffing: 0| 1| OFF| ON"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:STUFfing?')
		return Conversions.str_to_bool(response)
