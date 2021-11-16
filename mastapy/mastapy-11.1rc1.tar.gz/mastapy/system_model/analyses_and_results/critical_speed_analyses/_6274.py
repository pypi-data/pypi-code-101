'''_6274.py

ConceptGearSetCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2247
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6542
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6272, _6273, _6305
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ConceptGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCriticalSpeedAnalysis',)


class ConceptGearSetCriticalSpeedAnalysis(_6305.GearSetCriticalSpeedAnalysis):
    '''ConceptGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2247.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6542.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6542.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def concept_gears_critical_speed_analysis(self) -> 'List[_6272.ConceptGearCriticalSpeedAnalysis]':
        '''List[ConceptGearCriticalSpeedAnalysis]: 'ConceptGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsCriticalSpeedAnalysis, constructor.new(_6272.ConceptGearCriticalSpeedAnalysis))
        return value

    @property
    def concept_meshes_critical_speed_analysis(self) -> 'List[_6273.ConceptGearMeshCriticalSpeedAnalysis]':
        '''List[ConceptGearMeshCriticalSpeedAnalysis]: 'ConceptMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesCriticalSpeedAnalysis, constructor.new(_6273.ConceptGearMeshCriticalSpeedAnalysis))
        return value
