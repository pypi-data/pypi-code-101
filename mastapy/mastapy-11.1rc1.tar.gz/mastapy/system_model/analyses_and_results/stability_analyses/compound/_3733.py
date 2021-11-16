'''_3733.py

TorqueConverterConnectionCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2079
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3603
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3653
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'TorqueConverterConnectionCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionCompoundStabilityAnalysis',)


class TorqueConverterConnectionCompoundStabilityAnalysis(_3653.CouplingConnectionCompoundStabilityAnalysis):
    '''TorqueConverterConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2079.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.TorqueConverterConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2079.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3603.TorqueConverterConnectionStabilityAnalysis]':
        '''List[TorqueConverterConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3603.TorqueConverterConnectionStabilityAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3603.TorqueConverterConnectionStabilityAnalysis]':
        '''List[TorqueConverterConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3603.TorqueConverterConnectionStabilityAnalysis))
        return value
