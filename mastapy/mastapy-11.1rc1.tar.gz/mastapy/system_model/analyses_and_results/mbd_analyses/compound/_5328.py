'''_5328.py

RingPinsCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2295
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5187
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5316
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'RingPinsCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsCompoundMultibodyDynamicsAnalysis',)


class RingPinsCompoundMultibodyDynamicsAnalysis(_5316.MountableComponentCompoundMultibodyDynamicsAnalysis):
    '''RingPinsCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2295.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2295.RingPins)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5187.RingPinsMultibodyDynamicsAnalysis]':
        '''List[RingPinsMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5187.RingPinsMultibodyDynamicsAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5187.RingPinsMultibodyDynamicsAnalysis]':
        '''List[RingPinsMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5187.RingPinsMultibodyDynamicsAnalysis))
        return value
