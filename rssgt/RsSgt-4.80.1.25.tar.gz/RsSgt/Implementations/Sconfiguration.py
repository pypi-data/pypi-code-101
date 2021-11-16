from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sconfiguration:
	"""Sconfiguration commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sconfiguration", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BbSystemConfiguration:
		"""SCPI: SCONfiguration:MODE \n
		Snippet: value: enums.BbSystemConfiguration = driver.sconfiguration.get_mode() \n
		Switches between standard mode and ARB mode for envelope tracking. \n
			:return: configuration: STANdard| AFETracking STANdard Standard mode used for signal generation. AFETracking ARB foe Envelope Tracking: enables the usage of an extra baseband for enabling the envelope tracking ARB generation.
		"""
		response = self._core.io.query_str('SCONfiguration:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BbSystemConfiguration)

	def set_mode(self, configuration: enums.BbSystemConfiguration) -> None:
		"""SCPI: SCONfiguration:MODE \n
		Snippet: driver.sconfiguration.set_mode(configuration = enums.BbSystemConfiguration.AFETracking) \n
		Switches between standard mode and ARB mode for envelope tracking. \n
			:param configuration: STANdard| AFETracking STANdard Standard mode used for signal generation. AFETracking ARB foe Envelope Tracking: enables the usage of an extra baseband for enabling the envelope tracking ARB generation.
		"""
		param = Conversions.enum_scalar_to_str(configuration, enums.BbSystemConfiguration)
		self._core.io.write(f'SCONfiguration:MODE {param}')
