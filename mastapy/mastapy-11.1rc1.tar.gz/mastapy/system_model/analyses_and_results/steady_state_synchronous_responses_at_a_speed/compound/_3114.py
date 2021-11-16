'''_3114.py

ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2069
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2983
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3130
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed',)


class ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed(_3130.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed):
    '''ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2069.ClutchConnection':
        '''ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2069.ClutchConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2069.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2069.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2983.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]':
        '''List[ClutchConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2983.ClutchConnectionSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2983.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]':
        '''List[ClutchConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2983.ClutchConnectionSteadyStateSynchronousResponseAtASpeed))
        return value
