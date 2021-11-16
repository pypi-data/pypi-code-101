'''_5315.py

MeasurementComponentCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2189
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5174
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5361
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'MeasurementComponentCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundMultibodyDynamicsAnalysis',)


class MeasurementComponentCompoundMultibodyDynamicsAnalysis(_5361.VirtualComponentCompoundMultibodyDynamicsAnalysis):
    '''MeasurementComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2189.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2189.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5174.MeasurementComponentMultibodyDynamicsAnalysis]':
        '''List[MeasurementComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5174.MeasurementComponentMultibodyDynamicsAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5174.MeasurementComponentMultibodyDynamicsAnalysis]':
        '''List[MeasurementComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5174.MeasurementComponentMultibodyDynamicsAnalysis))
        return value
