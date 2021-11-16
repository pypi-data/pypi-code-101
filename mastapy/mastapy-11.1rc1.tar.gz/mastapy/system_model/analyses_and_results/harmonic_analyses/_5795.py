'''_5795.py

TorqueConverterTurbineHarmonicAnalysis
'''


from mastapy.system_model.part_model.couplings import _2335
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6679
from mastapy.system_model.analyses_and_results.system_deflections import _2551
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'TorqueConverterTurbineHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineHarmonicAnalysis',)


class TorqueConverterTurbineHarmonicAnalysis(_5687.CouplingHalfHarmonicAnalysis):
    '''TorqueConverterTurbineHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineHarmonicAnalysis.TYPE'):
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

    @property
    def system_deflection_results(self) -> '_2551.TorqueConverterTurbineSystemDeflection':
        '''TorqueConverterTurbineSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2551.TorqueConverterTurbineSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
