from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:HOSTname \n
		Snippet: value: str = driver.system.communicate.network.common.get_hostname() \n
		Sets the individual host name of the R&S SGT. Note: it is recommended that you do not change the host name in order to
		avoid problems with the networdk connection. However, if you change the host name be sure to use an unique name. The host
		name is a protected parameter, To change it, first disable protection level 1 with command SYSTem. \n
			:return: hostname: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:COMMon:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, hostname: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:HOSTname \n
		Snippet: driver.system.communicate.network.common.set_hostname(hostname = '1') \n
		Sets the individual host name of the R&S SGT. Note: it is recommended that you do not change the host name in order to
		avoid problems with the networdk connection. However, if you change the host name be sure to use an unique name. The host
		name is a protected parameter, To change it, first disable protection level 1 with command SYSTem. \n
			:param hostname: string
		"""
		param = Conversions.value_to_quoted_str(hostname)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:COMMon:HOSTname {param}')
