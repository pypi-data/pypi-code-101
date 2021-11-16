from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	# noinspection PyTypeChecker
	def get_border(self) -> enums.ByteOrder:
		"""SCPI: FORMat:BORDer \n
		Snippet: value: enums.ByteOrder = driver.formatPy.get_border() \n
		Determines the sequence of bytes within a binary block. This only affects blocks which use the IEEE754 format internally. \n
			:return: border: NORMal| SWAPped NORMal The instrument expects (with setting commands) and sends (with queries) the least significant byte of each IEEE754 floating-point number first and the most significant byte last. SWAPped The instrument expects (with setting commands) and sends (with queries) the most significant byte of each IEEE754 floating-point number first and the least significant byte last.
		"""
		response = self._core.io.query_str('FORMat:BORDer?')
		return Conversions.str_to_scalar_enum(response, enums.ByteOrder)

	def set_border(self, border: enums.ByteOrder) -> None:
		"""SCPI: FORMat:BORDer \n
		Snippet: driver.formatPy.set_border(border = enums.ByteOrder.NORMal) \n
		Determines the sequence of bytes within a binary block. This only affects blocks which use the IEEE754 format internally. \n
			:param border: NORMal| SWAPped NORMal The instrument expects (with setting commands) and sends (with queries) the least significant byte of each IEEE754 floating-point number first and the most significant byte last. SWAPped The instrument expects (with setting commands) and sends (with queries) the most significant byte of each IEEE754 floating-point number first and the least significant byte last.
		"""
		param = Conversions.enum_scalar_to_str(border, enums.ByteOrder)
		self._core.io.write(f'FORMat:BORDer {param}')

	# noinspection PyTypeChecker
	def get_sregister(self) -> enums.FormStatReg:
		"""SCPI: FORMat:SREGister \n
		Snippet: value: enums.FormStatReg = driver.formatPy.get_sregister() \n
		Determines the numerical format which is returned when the status registers are queried. \n
			:return: format_py: ASCii| BINary| HEXadecimal| OCTal ASCii The register content is returned as a decimal number. BINary The register content is returned as a binary number. #B is placed in front of the number. HEXadecimal The register content is returned as a hexadecimal number. #H is placed in front of the number. OCTal The register content is returned as an octal number. #Q is placed in front of the number.
		"""
		response = self._core.io.query_str('FORMat:SREGister?')
		return Conversions.str_to_scalar_enum(response, enums.FormStatReg)

	def set_sregister(self, format_py: enums.FormStatReg) -> None:
		"""SCPI: FORMat:SREGister \n
		Snippet: driver.formatPy.set_sregister(format_py = enums.FormStatReg.ASCii) \n
		Determines the numerical format which is returned when the status registers are queried. \n
			:param format_py: ASCii| BINary| HEXadecimal| OCTal ASCii The register content is returned as a decimal number. BINary The register content is returned as a binary number. #B is placed in front of the number. HEXadecimal The register content is returned as a hexadecimal number. #H is placed in front of the number. OCTal The register content is returned as an octal number. #Q is placed in front of the number.
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.FormStatReg)
		self._core.io.write(f'FORMat:SREGister {param}')

	# noinspection PyTypeChecker
	def get_data(self) -> enums.FormData:
		"""SCPI: FORMat:[DATA] \n
		Snippet: value: enums.FormData = driver.formatPy.get_data() \n
		Determines the data format which the R&S SGT uses to return data. When data is transferred from the control computer to
		the instrument, the instrument detects the data format automatically. In this case, the value set here is irrelevant. \n
			:return: data: ASCii| PACKed ASCii Numerical data is transferred as plain text separated by commas. PACKed Numerical data is transferred as binary block data. The format within the binary data depends on the command. The various binary data formats are explained in the description of the parameter types.
		"""
		response = self._core.io.query_str('FORMat:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.FormData)

	def set_data(self, data: enums.FormData) -> None:
		"""SCPI: FORMat:[DATA] \n
		Snippet: driver.formatPy.set_data(data = enums.FormData.ASCii) \n
		Determines the data format which the R&S SGT uses to return data. When data is transferred from the control computer to
		the instrument, the instrument detects the data format automatically. In this case, the value set here is irrelevant. \n
			:param data: ASCii| PACKed ASCii Numerical data is transferred as plain text separated by commas. PACKed Numerical data is transferred as binary block data. The format within the binary data depends on the command. The various binary data formats are explained in the description of the parameter types.
		"""
		param = Conversions.enum_scalar_to_str(data, enums.FormData)
		self._core.io.write(f'FORMat:DATA {param}')
