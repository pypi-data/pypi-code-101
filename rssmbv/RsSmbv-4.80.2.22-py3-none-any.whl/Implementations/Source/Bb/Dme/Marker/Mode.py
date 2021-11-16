from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AvionicMarkMode, marker=repcap.Marker.Default) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:DME:MARKer<CH>:MODE \n
		Snippet: driver.source.bb.dme.marker.mode.set(mode = enums.AvionicMarkMode.FP50P, marker = repcap.Marker.Default) \n
		Sets the mode for the selected marker. \n
			:param mode: FPSTart| FP50P| PSTart| P50P| PRECeived FPSTart: first pulse start FP50: first pulse 50% PSTart: pulse start P50: pulse 50% PRECeived: received pulse
			:param marker: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AvionicMarkMode)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:MARKer{marker_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, marker=repcap.Marker.Default) -> enums.AvionicMarkMode:
		"""SCPI: [SOURce<HW>]:[BB]:DME:MARKer<CH>:MODE \n
		Snippet: value: enums.AvionicMarkMode = driver.source.bb.dme.marker.mode.get(marker = repcap.Marker.Default) \n
		Sets the mode for the selected marker. \n
			:param marker: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Marker')
			:return: mode: FPSTart| FP50P| PSTart| P50P| PRECeived FPSTart: first pulse start FP50: first pulse 50% PSTart: pulse start P50: pulse 50% PRECeived: received pulse"""
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DME:MARKer{marker_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AvionicMarkMode)
