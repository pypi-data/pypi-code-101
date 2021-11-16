'''_6294.py

CylindricalGearSetCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2251, _2267
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6564, _6636
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6292, _6293, _6305
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CylindricalGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCriticalSpeedAnalysis',)


class CylindricalGearSetCriticalSpeedAnalysis(_6305.GearSetCriticalSpeedAnalysis):
    '''CylindricalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2251.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2251.CylindricalGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6564.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6564.CylindricalGearSetLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to CylindricalGearSetLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def cylindrical_gears_critical_speed_analysis(self) -> 'List[_6292.CylindricalGearCriticalSpeedAnalysis]':
        '''List[CylindricalGearCriticalSpeedAnalysis]: 'CylindricalGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsCriticalSpeedAnalysis, constructor.new(_6292.CylindricalGearCriticalSpeedAnalysis))
        return value

    @property
    def cylindrical_meshes_critical_speed_analysis(self) -> 'List[_6293.CylindricalGearMeshCriticalSpeedAnalysis]':
        '''List[CylindricalGearMeshCriticalSpeedAnalysis]: 'CylindricalMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesCriticalSpeedAnalysis, constructor.new(_6293.CylindricalGearMeshCriticalSpeedAnalysis))
        return value
