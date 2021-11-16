'''_3928.py

CycloidalDiscCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2294
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3796
from mastapy.system_model.analyses_and_results.power_flows.compound import _3884
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CycloidalDiscCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCompoundPowerFlow',)


class CycloidalDiscCompoundPowerFlow(_3884.AbstractShaftCompoundPowerFlow):
    '''CycloidalDiscCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_DISC_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2294.CycloidalDisc':
        '''CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2294.CycloidalDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3796.CycloidalDiscPowerFlow]':
        '''List[CycloidalDiscPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3796.CycloidalDiscPowerFlow))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3796.CycloidalDiscPowerFlow]':
        '''List[CycloidalDiscPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3796.CycloidalDiscPowerFlow))
        return value
