'''_4300.py

BevelDifferentialGearModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.gears import _2240, _2242, _2243
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6522, _6525, _6526
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4305
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'BevelDifferentialGearModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearModalAnalysisAtAStiffness',)


class BevelDifferentialGearModalAnalysisAtAStiffness(_4305.BevelGearModalAnalysisAtAStiffness):
    '''BevelDifferentialGearModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2240.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2240.BevelDifferentialGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6522.BevelDifferentialGearLoadCase':
        '''BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6522.BevelDifferentialGearLoadCase.TYPE not in self.wrapped.ComponentLoadCase.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to BevelDifferentialGearLoadCase. Expected: {}.'.format(self.wrapped.ComponentLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentLoadCase.__class__)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
