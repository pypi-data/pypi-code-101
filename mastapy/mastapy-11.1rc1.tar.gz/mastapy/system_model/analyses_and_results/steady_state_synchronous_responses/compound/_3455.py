'''_3455.py

SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.gears import _2269
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3453, _3454, _3372
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3322
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'SpiralBevelGearSetCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundSteadyStateSynchronousResponse',)


class SpiralBevelGearSetCompoundSteadyStateSynchronousResponse(_3372.BevelGearSetCompoundSteadyStateSynchronousResponse):
    '''SpiralBevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def spiral_bevel_gears_compound_steady_state_synchronous_response(self) -> 'List[_3453.SpiralBevelGearCompoundSteadyStateSynchronousResponse]':
        '''List[SpiralBevelGearCompoundSteadyStateSynchronousResponse]: 'SpiralBevelGearsCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundSteadyStateSynchronousResponse, constructor.new(_3453.SpiralBevelGearCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def spiral_bevel_meshes_compound_steady_state_synchronous_response(self) -> 'List[_3454.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse]':
        '''List[SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse]: 'SpiralBevelMeshesCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundSteadyStateSynchronousResponse, constructor.new(_3454.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3322.SpiralBevelGearSetSteadyStateSynchronousResponse]':
        '''List[SpiralBevelGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3322.SpiralBevelGearSetSteadyStateSynchronousResponse))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3322.SpiralBevelGearSetSteadyStateSynchronousResponse]':
        '''List[SpiralBevelGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3322.SpiralBevelGearSetSteadyStateSynchronousResponse))
        return value
