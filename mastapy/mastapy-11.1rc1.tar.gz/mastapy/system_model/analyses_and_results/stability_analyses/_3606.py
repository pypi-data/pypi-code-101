'''_3606.py

TorqueConverterTurbineStabilityAnalysis
'''


from mastapy.system_model.part_model.couplings import _2335
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6679
from mastapy.system_model.analyses_and_results.stability_analyses import _3521
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'TorqueConverterTurbineStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineStabilityAnalysis',)


class TorqueConverterTurbineStabilityAnalysis(_3521.CouplingHalfStabilityAnalysis):
    '''TorqueConverterTurbineStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineStabilityAnalysis.TYPE'):
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
    def component_load_case(self) -> '_6679.TorqueConverterTurbineLoadCase':
        '''TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6679.TorqueConverterTurbineLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
