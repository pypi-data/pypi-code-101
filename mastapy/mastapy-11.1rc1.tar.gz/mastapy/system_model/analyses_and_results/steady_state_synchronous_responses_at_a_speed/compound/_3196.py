'''_3196.py

SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2326
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3065
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3131
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed',)


class SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed(_3131.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed):
    '''SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2326.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2326.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3065.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpringDamperHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3065.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3065.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpringDamperHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3065.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed))
        return value
