'''_3335.py

StraightBevelGearSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.gears import _2272
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6666
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3239
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'StraightBevelGearSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSteadyStateSynchronousResponse',)


class StraightBevelGearSteadyStateSynchronousResponse(_3239.BevelGearSteadyStateSynchronousResponse):
    '''StraightBevelGearSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2272.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2272.StraightBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6666.StraightBevelGearLoadCase':
        '''StraightBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6666.StraightBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
