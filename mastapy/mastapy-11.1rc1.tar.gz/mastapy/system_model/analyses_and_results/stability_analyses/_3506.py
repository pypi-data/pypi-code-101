'''_3506.py

ClutchStabilityAnalysis
'''


from mastapy.system_model.part_model.couplings import _2303
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6534
from mastapy.system_model.analyses_and_results.stability_analyses import _3522
from mastapy._internal.python_net import python_net_import

_CLUTCH_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ClutchStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchStabilityAnalysis',)


class ClutchStabilityAnalysis(_3522.CouplingStabilityAnalysis):
    '''ClutchStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2303.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2303.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6534.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6534.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
