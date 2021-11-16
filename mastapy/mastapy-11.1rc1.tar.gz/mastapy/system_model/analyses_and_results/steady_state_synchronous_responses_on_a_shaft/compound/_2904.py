'''_2904.py

KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2264
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _2902, _2903, _2901
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2773
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_2901.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    '''KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2902.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2902.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2903.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2903.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2773.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2773.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2773.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2773.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft))
        return value
