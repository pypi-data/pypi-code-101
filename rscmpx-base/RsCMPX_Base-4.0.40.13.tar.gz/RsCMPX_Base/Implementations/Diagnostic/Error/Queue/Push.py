from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Push:
	"""Push commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("push", core, parent)

	def set(self, code: int, text: str, guid: str, info: str) -> None:
		"""SCPI: DIAGnostic:ERRor:QUEue:PUSH \n
		Snippet: driver.diagnostic.error.queue.push.set(code = 1, text = '1', guid = '1', info = '1') \n
		No command help available \n
			:param code: No help available
			:param text: No help available
			:param guid: No help available
			:param info: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('code', code, DataType.Integer), ArgSingle('text', text, DataType.String), ArgSingle('guid', guid, DataType.String), ArgSingle('info', info, DataType.String))
		self._core.io.write(f'DIAGnostic:ERRor:QUEue:PUSH {param}'.rstrip())
