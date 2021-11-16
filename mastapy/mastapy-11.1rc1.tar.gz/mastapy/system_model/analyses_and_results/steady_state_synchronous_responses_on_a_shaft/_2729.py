'''_2729.py

ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
'''


from mastapy.system_model.connections_and_sockets.couplings import _2071
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6537
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2740
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft',)


class ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft(_2740.CouplingConnectionSteadyStateSynchronousResponseOnAShaft):
    '''ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2071.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6537.ConceptCouplingConnectionLoadCase':
        '''ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6537.ConceptCouplingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
