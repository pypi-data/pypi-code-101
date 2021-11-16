from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utc:
	"""Utc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utc", core, parent)

	def get_create(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:UTC:CREate \n
		Snippet: value: str = driver.source.bb.gnss.adGeneration.utc.get_create() \n
		Stores the current assistance data settings into the selected UTC file. The file extension (*.rs_utc) is assigned
		automatically. Refer to 'MMEMory Subsystem' for general information on file handling in the default and in a specific
		directory. \n
			:return: filename: string Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:UTC:CREate?')
		return trim_str_response(response)

	def set_create(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:UTC:CREate \n
		Snippet: driver.source.bb.gnss.adGeneration.utc.set_create(filename = '1') \n
		Stores the current assistance data settings into the selected UTC file. The file extension (*.rs_utc) is assigned
		automatically. Refer to 'MMEMory Subsystem' for general information on file handling in the default and in a specific
		directory. \n
			:param filename: string Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:UTC:CREate {param}')
