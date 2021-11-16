'''_4393.py

SpringDamperModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.couplings import _2325
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6662
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4327
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'SpringDamperModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperModalAnalysisAtAStiffness',)


class SpringDamperModalAnalysisAtAStiffness(_4327.CouplingModalAnalysisAtAStiffness):
    '''SpringDamperModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2325.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2325.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6662.SpringDamperLoadCase':
        '''SpringDamperLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6662.SpringDamperLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
