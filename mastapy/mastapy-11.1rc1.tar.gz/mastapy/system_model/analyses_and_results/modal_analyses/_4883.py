'''_4883.py

MeasurementComponentModalAnalysis
'''


from mastapy.system_model.part_model import _2189
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6624
from mastapy.system_model.analyses_and_results.system_deflections import _2500
from mastapy.system_model.analyses_and_results.modal_analyses import _4934
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'MeasurementComponentModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentModalAnalysis',)


class MeasurementComponentModalAnalysis(_4934.VirtualComponentModalAnalysis):
    '''MeasurementComponentModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentModalAnalysis.TYPE'):
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
    def component_load_case(self) -> '_6624.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6624.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2500.MeasurementComponentSystemDeflection':
        '''MeasurementComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2500.MeasurementComponentSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
