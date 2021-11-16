'''_3456.py

SpringDamperCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2325
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3326
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3391
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'SpringDamperCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperCompoundSteadyStateSynchronousResponse',)


class SpringDamperCompoundSteadyStateSynchronousResponse(_3391.CouplingCompoundSteadyStateSynchronousResponse):
    '''SpringDamperCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2325.SpringDamper':
        '''SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2325.SpringDamper)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2325.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2325.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3326.SpringDamperSteadyStateSynchronousResponse]':
        '''List[SpringDamperSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3326.SpringDamperSteadyStateSynchronousResponse))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3326.SpringDamperSteadyStateSynchronousResponse]':
        '''List[SpringDamperSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3326.SpringDamperSteadyStateSynchronousResponse))
        return value
