from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identification:
	"""Identification commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identification", core, parent)

	def preset(self) -> None:
		"""SCPI: SYSTem:IDENtification:PRESet \n
		Snippet: driver.system.identification.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:IDENtification:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:IDENtification:PRESet \n
		Snippet: driver.system.identification.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:IDENtification:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.IecDevId:
		"""SCPI: SYSTem:IDENtification \n
		Snippet: value: enums.IecDevId = driver.system.identification.get_value() \n
		Selects the mode the instrument identification is performed. \n
			:return: identification: AUTO| USER AUTO The *IDN string and the *OPT string are set automatically. USER Enables the selection of user definable *IDN and *OPT strings.
		"""
		response = self._core.io.query_str('SYSTem:IDENtification?')
		return Conversions.str_to_scalar_enum(response, enums.IecDevId)

	def set_value(self, identification: enums.IecDevId) -> None:
		"""SCPI: SYSTem:IDENtification \n
		Snippet: driver.system.identification.set_value(identification = enums.IecDevId.AUTO) \n
		Selects the mode the instrument identification is performed. \n
			:param identification: AUTO| USER AUTO The *IDN string and the *OPT string are set automatically. USER Enables the selection of user definable *IDN and *OPT strings.
		"""
		param = Conversions.enum_scalar_to_str(identification, enums.IecDevId)
		self._core.io.write(f'SYSTem:IDENtification {param}')
