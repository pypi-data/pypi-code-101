'''_3407.py

FaceGearCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.gears import _2253
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3277
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3412
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'FaceGearCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearCompoundSteadyStateSynchronousResponse',)


class FaceGearCompoundSteadyStateSynchronousResponse(_3412.GearCompoundSteadyStateSynchronousResponse):
    '''FaceGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2253.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2253.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3277.FaceGearSteadyStateSynchronousResponse]':
        '''List[FaceGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3277.FaceGearSteadyStateSynchronousResponse))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3277.FaceGearSteadyStateSynchronousResponse]':
        '''List[FaceGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3277.FaceGearSteadyStateSynchronousResponse))
        return value
