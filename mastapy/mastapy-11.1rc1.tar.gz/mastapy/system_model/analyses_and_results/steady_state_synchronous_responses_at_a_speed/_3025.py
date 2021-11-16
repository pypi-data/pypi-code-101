'''_3025.py

HypoidGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2260
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6609
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3026, _3024, _2967
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'HypoidGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSteadyStateSynchronousResponseAtASpeed',)


class HypoidGearSetSteadyStateSynchronousResponseAtASpeed(_2967.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed):
    '''HypoidGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2260.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6609.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6609.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def hypoid_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3026.HypoidGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearSteadyStateSynchronousResponseAtASpeed]: 'HypoidGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_3026.HypoidGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def hypoid_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3024.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearMeshSteadyStateSynchronousResponseAtASpeed]: 'HypoidMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_3024.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
