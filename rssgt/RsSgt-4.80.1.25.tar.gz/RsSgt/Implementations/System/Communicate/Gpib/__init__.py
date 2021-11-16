from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gpib:
	"""Gpib commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gpib", core, parent)

	@property
	def self(self):
		"""self commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_self'):
			from .Self import Self
			self._self = Self(self._core, self._cmd_group)
		return self._self

	# noinspection PyTypeChecker
	def get_lterminator(self) -> enums.IecTermMode:
		"""SCPI: SYSTem:COMMunicate:GPIB:LTERminator \n
		Snippet: value: enums.IecTermMode = driver.system.communicate.gpib.get_lterminator() \n
		Sets the terminator recognition for remote control via GPIB bus. \n
			:return: lterminator: STANdard| EOI EOI The terminator must be sent together with the line message EOI (End of Line) . This setting is recommended for binary block transmissions where a character could coincidentally have the value LF (Line Feed) but is not intended as the terminator. This setting must be selected for block data with undefined length. STANdard An LF (Line Feed) is recognized as the terminator regardless of whether it is sent with or without EOI.
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:GPIB:LTERminator?')
		return Conversions.str_to_scalar_enum(response, enums.IecTermMode)

	def set_lterminator(self, lterminator: enums.IecTermMode) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB:LTERminator \n
		Snippet: driver.system.communicate.gpib.set_lterminator(lterminator = enums.IecTermMode.EOI) \n
		Sets the terminator recognition for remote control via GPIB bus. \n
			:param lterminator: STANdard| EOI EOI The terminator must be sent together with the line message EOI (End of Line) . This setting is recommended for binary block transmissions where a character could coincidentally have the value LF (Line Feed) but is not intended as the terminator. This setting must be selected for block data with undefined length. STANdard An LF (Line Feed) is recognized as the terminator regardless of whether it is sent with or without EOI.
		"""
		param = Conversions.enum_scalar_to_str(lterminator, enums.IecTermMode)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:LTERminator {param}')

	def get_resource(self) -> str:
		"""SCPI: SYSTem:COMMunicate:GPIB:RESource \n
		Snippet: value: str = driver.system.communicate.gpib.get_resource() \n
		Queries the VISA resource string for remote control via the GPIB interface. To change the GPIB address, use the command
		SYSTem:COMMunicate:ADDRess. \n
			:return: resource: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:GPIB:RESource?')
		return trim_str_response(response)

	def clone(self) -> 'Gpib':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gpib(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
