from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Create:
	"""Create commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("create", core, parent)

	def set_named(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:AWGN:CREate:NAMed \n
		Snippet: driver.source.bb.arbitrary.tsignal.awgn.create.set_named(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TSIGnal:AWGN:CREate:NAMed {param}')
