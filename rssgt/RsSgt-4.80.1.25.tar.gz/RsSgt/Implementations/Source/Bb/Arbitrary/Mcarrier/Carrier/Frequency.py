from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:FREQuency \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.frequency.set(frequency = 1, carrier = repcap.Carrier.Default) \n
		Sets or indicates the carrier frequency, depending on the selected carrier frequency mode. The carrier frequency can be
		set in 'Arbitrary Carrier frequency' mode. For 'Equidistant Carrier Spacing', the carrier spacing is determined
		automatically. \n
			:param frequency: float Value range depends on the max bandwidth, see data sheet Range: -40E6 to 40E6
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:FREQuency {param}')

	def get(self, carrier=repcap.Carrier.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:FREQuency \n
		Snippet: value: int = driver.source.bb.arbitrary.mcarrier.carrier.frequency.get(carrier = repcap.Carrier.Default) \n
		Sets or indicates the carrier frequency, depending on the selected carrier frequency mode. The carrier frequency can be
		set in 'Arbitrary Carrier frequency' mode. For 'Equidistant Carrier Spacing', the carrier spacing is determined
		automatically. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
			:return: frequency: float Value range depends on the max bandwidth, see data sheet Range: -40E6 to 40E6"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:FREQuency?')
		return Conversions.str_to_int(response)
