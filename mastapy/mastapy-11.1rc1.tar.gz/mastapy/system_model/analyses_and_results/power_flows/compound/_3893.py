'''_3893.py

BeltDriveCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2301, _2311
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.power_flows import _3760
from mastapy.system_model.analyses_and_results.power_flows.compound import _3981
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BeltDriveCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveCompoundPowerFlow',)


class BeltDriveCompoundPowerFlow(_3981.SpecialisedAssemblyCompoundPowerFlow):
    '''BeltDriveCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2301.BeltDrive':
        '''BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2301.BeltDrive.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltDrive. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2301.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2301.BeltDrive.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BeltDrive. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3760.BeltDrivePowerFlow]':
        '''List[BeltDrivePowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3760.BeltDrivePowerFlow))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3760.BeltDrivePowerFlow]':
        '''List[BeltDrivePowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3760.BeltDrivePowerFlow))
        return value
