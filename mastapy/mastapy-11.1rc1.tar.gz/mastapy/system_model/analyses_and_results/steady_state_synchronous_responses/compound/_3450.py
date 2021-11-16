'''_3450.py

ShaftHubConnectionCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3317
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3390
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'ShaftHubConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionCompoundSteadyStateSynchronousResponse',)


class ShaftHubConnectionCompoundSteadyStateSynchronousResponse(_3390.ConnectorCompoundSteadyStateSynchronousResponse):
    '''ShaftHubConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2323.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2323.ShaftHubConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3317.ShaftHubConnectionSteadyStateSynchronousResponse]':
        '''List[ShaftHubConnectionSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3317.ShaftHubConnectionSteadyStateSynchronousResponse))
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionCompoundSteadyStateSynchronousResponse]':
        '''List[ShaftHubConnectionCompoundSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftHubConnectionCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3317.ShaftHubConnectionSteadyStateSynchronousResponse]':
        '''List[ShaftHubConnectionSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3317.ShaftHubConnectionSteadyStateSynchronousResponse))
        return value
