'''_3048.py

PointLoadSteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model import _2197
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6641
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3085
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'PointLoadSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadSteadyStateSynchronousResponseAtASpeed',)


class PointLoadSteadyStateSynchronousResponseAtASpeed(_3085.VirtualComponentSteadyStateSynchronousResponseAtASpeed):
    '''PointLoadSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2197.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2197.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6641.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6641.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
