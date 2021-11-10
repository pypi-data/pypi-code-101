from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speed:
	"""Speed commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speed", core, parent)

	def set(self, areg_object_dopp: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:DOPPler:[SPEed] \n
		Snippet: driver.source.areGenerator.object.doppler.speed.set(areg_object_dopp = 1.0, objectIx = repcap.ObjectIx.Default) \n
		If [:SOURce<hw>]:AREGenerator:UNITs:DOPPlerSPEed, sets the Doppler speed of a specific object. \n
			:param areg_object_dopp: float If you do no specify a speed unit, the default unit is used. Range: -500 to 500, Unit: km/h
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(areg_object_dopp)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:DOPPler:SPEed {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:DOPPler:[SPEed] \n
		Snippet: value: float = driver.source.areGenerator.object.doppler.speed.get(objectIx = repcap.ObjectIx.Default) \n
		If [:SOURce<hw>]:AREGenerator:UNITs:DOPPlerSPEed, sets the Doppler speed of a specific object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: areg_object_dopp: float If you do no specify a speed unit, the default unit is used. Range: -500 to 500, Unit: km/h"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:DOPPler:SPEed?')
		return Conversions.str_to_float(response)
