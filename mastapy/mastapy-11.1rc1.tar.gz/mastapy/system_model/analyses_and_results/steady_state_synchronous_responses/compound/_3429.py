'''_3429.py

MassDiscCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model import _2188
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3297
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3476
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'MassDiscCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscCompoundSteadyStateSynchronousResponse',)


class MassDiscCompoundSteadyStateSynchronousResponse(_3476.VirtualComponentCompoundSteadyStateSynchronousResponse):
    '''MassDiscCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2188.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2188.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3297.MassDiscSteadyStateSynchronousResponse]':
        '''List[MassDiscSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3297.MassDiscSteadyStateSynchronousResponse))
        return value

    @property
    def planetaries(self) -> 'List[MassDiscCompoundSteadyStateSynchronousResponse]':
        '''List[MassDiscCompoundSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3297.MassDiscSteadyStateSynchronousResponse]':
        '''List[MassDiscSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3297.MassDiscSteadyStateSynchronousResponse))
        return value
