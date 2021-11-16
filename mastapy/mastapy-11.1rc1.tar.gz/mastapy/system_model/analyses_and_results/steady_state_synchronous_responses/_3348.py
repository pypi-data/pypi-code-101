'''_3348.py

WormGearMeshSteadyStateSynchronousResponse
'''


from mastapy.system_model.connections_and_sockets.gears import _2056
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6687
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3280
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'WormGearMeshSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshSteadyStateSynchronousResponse',)


class WormGearMeshSteadyStateSynchronousResponse(_3280.GearMeshSteadyStateSynchronousResponse):
    '''WormGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2056.WormGearMesh':
        '''WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.WormGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6687.WormGearMeshLoadCase':
        '''WormGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6687.WormGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
