from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def get_fast(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:STORe:FAST \n
		Snippet: value: bool = driver.source.bb.arbitrary.mcarrier.setting.store.get_fast() \n
		Determines whether the instrument performs an absolute or a differential storing of the settings. Enable this function to
		accelerate the saving process by saving only the settings with values different to the default ones. Note: This function
		is not affected by the 'Preset' function. \n
			:return: fast: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:STORe:FAST?')
		return Conversions.str_to_bool(response)

	def set_fast(self, fast: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:STORe:FAST \n
		Snippet: driver.source.bb.arbitrary.mcarrier.setting.store.set_fast(fast = False) \n
		Determines whether the instrument performs an absolute or a differential storing of the settings. Enable this function to
		accelerate the saving process by saving only the settings with values different to the default ones. Note: This function
		is not affected by the 'Preset' function. \n
			:param fast: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(fast)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:STORe:FAST {param}')

	def set_value(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:STORe \n
		Snippet: driver.source.bb.arbitrary.mcarrier.setting.store.set_value(filename = '1') \n
		The command stores the current settings of submenu 'Multi Carrier' in a file in the specified directory.
		The file extension may be omitted, the files are stored with the file extension *.arb_multcarr. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:STORe {param}')
