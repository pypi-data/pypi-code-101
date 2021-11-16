'''_3123.py

ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2247
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3121, _3122, _3152
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2992
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_3152.GearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    '''ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2247.ConceptGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2247.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def concept_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3121.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'ConceptGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_3121.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def concept_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3122.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'ConceptMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_3122.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2992.ConceptGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2992.ConceptGearSetSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2992.ConceptGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2992.ConceptGearSetSteadyStateSynchronousResponseAtASpeed))
        return value
