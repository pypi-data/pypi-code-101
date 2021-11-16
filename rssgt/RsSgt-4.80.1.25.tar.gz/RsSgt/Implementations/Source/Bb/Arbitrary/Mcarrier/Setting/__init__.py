from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.arbitrary.mcarrier.setting.get_catalog() \n
		Queries the available settings files in the specified default directory. The settings files are used to set the ARB multi
		carrier submenu. Only files with the file extension *.arb_multcarr will be listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:LOAD \n
		Snippet: driver.source.bb.arbitrary.mcarrier.setting.load(filename = '1') \n
		Loads the settings file. If a settings file with the specified name does not yet exist, it is created. The file extension
		may be omitted. Only files with the file extension *.arb_multcarr will be loaded or created. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:LOAD {param}')

	def clone(self) -> 'Setting':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Setting(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
