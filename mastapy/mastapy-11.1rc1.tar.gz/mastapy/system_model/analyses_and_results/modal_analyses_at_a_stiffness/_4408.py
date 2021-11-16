'''_4408.py

TorqueConverterPumpModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.couplings import _2333
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6678
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4326
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'TorqueConverterPumpModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpModalAnalysisAtAStiffness',)


class TorqueConverterPumpModalAnalysisAtAStiffness(_4326.CouplingHalfModalAnalysisAtAStiffness):
    '''TorqueConverterPumpModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2333.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2333.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6678.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6678.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
