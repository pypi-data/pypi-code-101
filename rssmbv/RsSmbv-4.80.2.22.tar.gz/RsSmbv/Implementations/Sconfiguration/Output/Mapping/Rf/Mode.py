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

	def set(self, mode: enums.SystConfOutpMapMatMode, path=repcap.Path.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:RF<CH>:MODE \n
		Snippet: driver.sconfiguration.output.mapping.rf.mode.set(mode = enums.SystConfOutpMapMatMode.ADD, path = repcap.Path.Default) \n
		No command help available \n
			:param mode: No help available
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMapMatMode)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:RF{path_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, path=repcap.Path.Default) -> enums.SystConfOutpMapMatMode:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:RF<CH>:MODE \n
		Snippet: value: enums.SystConfOutpMapMatMode = driver.sconfiguration.output.mapping.rf.mode.get(path = repcap.Path.Default) \n
		No command help available \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: mode: No help available"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:RF{path_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMapMatMode)
