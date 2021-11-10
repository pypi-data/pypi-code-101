from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, areg_obj_state: bool, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:[STATe] \n
		Snippet: driver.source.areGenerator.object.state.set(areg_obj_state = False, objectIx = repcap.ObjectIx.Default) \n
		Activates one of the available radar objects (1 to 4) . \n
			:param areg_obj_state: 0| 1| OFF| ON
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.bool_to_str(areg_obj_state)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:STATe {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJect<CH>:[STATe] \n
		Snippet: value: bool = driver.source.areGenerator.object.state.get(objectIx = repcap.ObjectIx.Default) \n
		Activates one of the available radar objects (1 to 4) . \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: areg_obj_state: 0| 1| OFF| ON"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:OBJect{objectIx_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
