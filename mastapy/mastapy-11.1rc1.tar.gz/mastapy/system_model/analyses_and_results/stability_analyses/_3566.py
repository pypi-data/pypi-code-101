'''_3566.py

PartToPartShearCouplingStabilityAnalysis
'''


from mastapy.system_model.part_model.couplings import _2313
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6634
from mastapy.system_model.analyses_and_results.stability_analyses import _3522
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'PartToPartShearCouplingStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingStabilityAnalysis',)


class PartToPartShearCouplingStabilityAnalysis(_3522.CouplingStabilityAnalysis):
    '''PartToPartShearCouplingStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2313.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.PartToPartShearCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6634.PartToPartShearCouplingLoadCase':
        '''PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6634.PartToPartShearCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
