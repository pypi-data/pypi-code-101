'''_3119.py

ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2071
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2988
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3130
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed(_3130.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed):
    '''ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2071.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ConceptCouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2071.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2988.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2988.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2988.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2988.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed))
        return value
