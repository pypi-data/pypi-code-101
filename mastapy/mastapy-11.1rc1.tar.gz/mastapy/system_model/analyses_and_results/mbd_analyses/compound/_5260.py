'''_5260.py

ClutchCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2303
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5112
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5276
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ClutchCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchCompoundMultibodyDynamicsAnalysis',)


class ClutchCompoundMultibodyDynamicsAnalysis(_5276.CouplingCompoundMultibodyDynamicsAnalysis):
    '''ClutchCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2303.Clutch':
        '''Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2303.Clutch)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2303.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2303.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5112.ClutchMultibodyDynamicsAnalysis]':
        '''List[ClutchMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5112.ClutchMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5112.ClutchMultibodyDynamicsAnalysis]':
        '''List[ClutchMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5112.ClutchMultibodyDynamicsAnalysis))
        return value
