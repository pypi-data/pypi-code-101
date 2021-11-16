'''_4649.py

SpringDamperConnectionModalAnalysisAtASpeed
'''


from mastapy.system_model.connections_and_sockets.couplings import _2077
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6660
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4584
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'SpringDamperConnectionModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionModalAnalysisAtASpeed',)


class SpringDamperConnectionModalAnalysisAtASpeed(_4584.CouplingConnectionModalAnalysisAtASpeed):
    '''SpringDamperConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2077.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2077.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6660.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6660.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
