from typing import List

from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, channelNull=repcap.ChannelNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:USER:CATalog \n
		Snippet: value: List[str] = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.user.catalog.get(channelNull = repcap.ChannelNull.Default) \n
		Queries existing files with stored user channel codings. The files are stored with the fixed file extensions *.3g_ccod_dl
		in a directory of the user's choice. The directory applicable to the commands is defined with the command method RsSmbv.
		MassMemory.currentDirectory. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: catalog: string"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:USER:CATalog?')
		return Conversions.str_to_str_list(response)
