'''_6370.py

WormGearSetCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2277
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6688
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6368, _6369, _6305
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'WormGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCriticalSpeedAnalysis',)


class WormGearSetCriticalSpeedAnalysis(_6305.GearSetCriticalSpeedAnalysis):
    '''WormGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2277.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2277.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6688.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6688.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def worm_gears_critical_speed_analysis(self) -> 'List[_6368.WormGearCriticalSpeedAnalysis]':
        '''List[WormGearCriticalSpeedAnalysis]: 'WormGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCriticalSpeedAnalysis, constructor.new(_6368.WormGearCriticalSpeedAnalysis))
        return value

    @property
    def worm_meshes_critical_speed_analysis(self) -> 'List[_6369.WormGearMeshCriticalSpeedAnalysis]':
        '''List[WormGearMeshCriticalSpeedAnalysis]: 'WormMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCriticalSpeedAnalysis, constructor.new(_6369.WormGearMeshCriticalSpeedAnalysis))
        return value
