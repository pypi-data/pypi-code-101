'''_4740.py

HypoidGearSetCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2260
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _4738, _4739, _4682
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4611
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'HypoidGearSetCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundModalAnalysisAtASpeed',)


class HypoidGearSetCompoundModalAnalysisAtASpeed(_4682.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed):
    '''HypoidGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2260.HypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2260.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def hypoid_gears_compound_modal_analysis_at_a_speed(self) -> 'List[_4738.HypoidGearCompoundModalAnalysisAtASpeed]':
        '''List[HypoidGearCompoundModalAnalysisAtASpeed]: 'HypoidGearsCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsCompoundModalAnalysisAtASpeed, constructor.new(_4738.HypoidGearCompoundModalAnalysisAtASpeed))
        return value

    @property
    def hypoid_meshes_compound_modal_analysis_at_a_speed(self) -> 'List[_4739.HypoidGearMeshCompoundModalAnalysisAtASpeed]':
        '''List[HypoidGearMeshCompoundModalAnalysisAtASpeed]: 'HypoidMeshesCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesCompoundModalAnalysisAtASpeed, constructor.new(_4739.HypoidGearMeshCompoundModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4611.HypoidGearSetModalAnalysisAtASpeed]':
        '''List[HypoidGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4611.HypoidGearSetModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4611.HypoidGearSetModalAnalysisAtASpeed]':
        '''List[HypoidGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4611.HypoidGearSetModalAnalysisAtASpeed))
        return value
