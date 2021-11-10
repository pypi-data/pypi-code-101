from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, areg_obj_att: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:ATTenuation \n
		Snippet: driver.source.areGenerator.object.attenuation.set(areg_obj_att = 1.0, objectIx = repcap.ObjectIx.Default) \n
		Sets the attenuation of a specific radar object. Together with the base attenuation that applies to all radar objects, it
		forms the total attenuation for the specific object. \n
			:param areg_obj_att: float Range: 0 to 63.5
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(areg_obj_att)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:ATTenuation {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:ATTenuation \n
		Snippet: value: float = driver.source.areGenerator.object.attenuation.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the attenuation of a specific radar object. Together with the base attenuation that applies to all radar objects, it
		forms the total attenuation for the specific object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: areg_obj_att: float Range: 0 to 63.5"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:ATTenuation?')
		return Conversions.str_to_float(response)
