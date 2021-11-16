from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Healthy:
	"""Healthy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("healthy", core, parent)

	def set(self, healthy_state: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:HEALthy \n
		Snippet: driver.source.bb.gnss.svid.gps.healthy.set(healthy_state = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param healthy_state: 0| 1| OFF| ON 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: BB:GNSS:SVIDch:GPS:NMESsage:LNAV:EPHemeris:HEALth BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L1Health BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L2Health BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L5Health BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BDVS BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BHS BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E5BHS BB:GNSS:SVIDch:BEIDou:NMESsage:DNAV:EPHemeris:HEALth BB:GNSS:SVIDch:GLONass:NMESsage:NAV:EPHemeris:HEALth BB:GNSS:SVIDch:QZSS:NMESsage:NAV:EPHemeris:HEALth The values are interdependent; changing one of them changes the other.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(healthy_state)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:HEALthy {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:HEALthy \n
		Snippet: value: bool = driver.source.bb.gnss.svid.gps.healthy.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: healthy_state: 0| 1| OFF| ON 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: BB:GNSS:SVIDch:GPS:NMESsage:LNAV:EPHemeris:HEALth BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L1Health BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L2Health BB:GNSS:SVIDch:GPS:NMESsage:CNAV:EPHemeris:L5Health BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BDVS BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E1BHS BB:GNSS:SVIDch:GALileo:NMESsage:INAV:E5BHS BB:GNSS:SVIDch:BEIDou:NMESsage:DNAV:EPHemeris:HEALth BB:GNSS:SVIDch:GLONass:NMESsage:NAV:EPHemeris:HEALth BB:GNSS:SVIDch:QZSS:NMESsage:NAV:EPHemeris:HEALth The values are interdependent; changing one of them changes the other."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:HEALthy?')
		return Conversions.str_to_bool(response)
