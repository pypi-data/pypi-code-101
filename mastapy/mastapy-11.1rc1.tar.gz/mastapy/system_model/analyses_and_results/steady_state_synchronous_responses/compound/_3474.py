'''_3474.py

TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2335
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3345
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3393
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'TorqueConverterTurbineCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineCompoundSteadyStateSynchronousResponse',)


class TorqueConverterTurbineCompoundSteadyStateSynchronousResponse(_3393.CouplingHalfCompoundSteadyStateSynchronousResponse):
    '''TorqueConverterTurbineCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2335.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2335.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3345.TorqueConverterTurbineSteadyStateSynchronousResponse]':
        '''List[TorqueConverterTurbineSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3345.TorqueConverterTurbineSteadyStateSynchronousResponse))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3345.TorqueConverterTurbineSteadyStateSynchronousResponse]':
        '''List[TorqueConverterTurbineSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3345.TorqueConverterTurbineSteadyStateSynchronousResponse))
        return value
