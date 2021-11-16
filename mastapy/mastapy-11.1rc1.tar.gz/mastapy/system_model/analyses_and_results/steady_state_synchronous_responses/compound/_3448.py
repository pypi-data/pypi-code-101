'''_3448.py

RootAssemblyCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3316
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3361
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'RootAssemblyCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundSteadyStateSynchronousResponse',)


class RootAssemblyCompoundSteadyStateSynchronousResponse(_3361.AssemblyCompoundSteadyStateSynchronousResponse):
    '''RootAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3316.RootAssemblySteadyStateSynchronousResponse]':
        '''List[RootAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3316.RootAssemblySteadyStateSynchronousResponse))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3316.RootAssemblySteadyStateSynchronousResponse]':
        '''List[RootAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3316.RootAssemblySteadyStateSynchronousResponse))
        return value
