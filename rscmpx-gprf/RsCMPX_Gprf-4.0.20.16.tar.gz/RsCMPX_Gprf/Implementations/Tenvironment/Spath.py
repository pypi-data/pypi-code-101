from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spath:
	"""Spath commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def delete(self, name_signal_path: str) -> None:
		"""SCPI: DELete:TENVironment:SPATh \n
		Snippet: driver.tenvironment.spath.delete(name_signal_path = '1') \n
		No command help available \n
			:param name_signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(name_signal_path)
		self._core.io.write(f'DELete:TENVironment:SPATh {param}')
