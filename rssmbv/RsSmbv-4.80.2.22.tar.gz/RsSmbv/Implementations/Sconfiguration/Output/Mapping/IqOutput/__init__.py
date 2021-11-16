from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOutput:
	"""IqOutput commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqOutput", core, parent)

	@property
	def stream(self):
		"""stream commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SystConfOutpMapMatMode:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:IQOutput:MODE \n
		Snippet: value: enums.SystConfOutpMapMatMode = driver.sconfiguration.output.mapping.iqOutput.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:OUTPut:MAPPing:IQOutput:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMapMatMode)

	def set_mode(self, mode: enums.SystConfOutpMapMatMode) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:IQOutput:MODE \n
		Snippet: driver.sconfiguration.output.mapping.iqOutput.set_mode(mode = enums.SystConfOutpMapMatMode.ADD) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMapMatMode)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:IQOutput:MODE {param}')

	def clone(self) -> 'IqOutput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqOutput(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
