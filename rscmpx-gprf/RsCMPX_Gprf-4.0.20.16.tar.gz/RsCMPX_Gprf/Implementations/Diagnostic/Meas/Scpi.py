from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scpi:
	"""Scpi commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scpi", core, parent)

	def get_version(self) -> float:
		"""SCPI: DIAGnostic:MEAS:SCPI:VERSion \n
		Snippet: value: float = driver.diagnostic.meas.scpi.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:MEAS:SCPI:VERSion?')
		return Conversions.str_to_float(response)
