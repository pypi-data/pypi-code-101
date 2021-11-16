from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 17 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def parameter(self):
		"""parameter commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_parameter'):
			from .Parameter import Parameter
			self._parameter = Parameter(self._core, self._cmd_group)
		return self._parameter

	def get_auto(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:AUTO \n
		Snippet: value: bool = driver.source.bb.huwb.filterPy.get_auto() \n
		Queries if the internal (''Auto'') filter is applied. This filter is selected automatically, if carrier aggregation with
		carriers that span different bandwidths is used. \n
			:return: auto: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:AUTO?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_osampling(self) -> enums.HrpUwbOverSampling:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:OSAMpling \n
		Snippet: value: enums.HrpUwbOverSampling = driver.source.bb.huwb.filterPy.get_osampling() \n
		Sets the oversampling factor of the generated waveform. A reduced sample rate saves significantly the amount of memory or
		allows an increased signal cycle time, and vice versa. \n
			:return: oversampling: OS_2| OS_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:OSAMpling?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbOverSampling)

	def set_osampling(self, oversampling: enums.HrpUwbOverSampling) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:OSAMpling \n
		Snippet: driver.source.bb.huwb.filterPy.set_osampling(oversampling = enums.HrpUwbOverSampling.OS_1) \n
		Sets the oversampling factor of the generated waveform. A reduced sample rate saves significantly the amount of memory or
		allows an increased signal cycle time, and vice versa. \n
			:param oversampling: OS_2| OS_1
		"""
		param = Conversions.enum_scalar_to_str(oversampling, enums.HrpUwbOverSampling)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FILTer:OSAMpling {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFilterB:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:TYPE \n
		Snippet: value: enums.DmFilterB = driver.source.bb.huwb.filterPy.get_type_py() \n
		Selects the baseband filter type. \n
			:return: type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| USER| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LTEFilter| LPASSEVM| APCO25Hcpm| APCO25Lsm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFilterB)

	def set_type_py(self, type_py: enums.DmFilterB) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:TYPE \n
		Snippet: driver.source.bb.huwb.filterPy.set_type_py(type_py = enums.DmFilterB.APCO25) \n
		Selects the baseband filter type. \n
			:param type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| USER| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LTEFilter| LPASSEVM| APCO25Hcpm| APCO25Lsm
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFilterB)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
