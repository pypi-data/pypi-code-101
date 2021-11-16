'''_3478.py

WormGearMeshCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2056
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3348
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3413
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'WormGearMeshCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshCompoundSteadyStateSynchronousResponse',)


class WormGearMeshCompoundSteadyStateSynchronousResponse(_3413.GearMeshCompoundSteadyStateSynchronousResponse):
    '''WormGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2056.WormGearMesh':
        '''WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.WormGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2056.WormGearMesh':
        '''WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.WormGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3348.WormGearMeshSteadyStateSynchronousResponse]':
        '''List[WormGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3348.WormGearMeshSteadyStateSynchronousResponse))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3348.WormGearMeshSteadyStateSynchronousResponse]':
        '''List[WormGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3348.WormGearMeshSteadyStateSynchronousResponse))
        return value
