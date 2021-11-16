'''_6326.py

PartToPartShearCouplingCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model.couplings import _2313
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6634
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6281
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PartToPartShearCouplingCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCriticalSpeedAnalysis',)


class PartToPartShearCouplingCriticalSpeedAnalysis(_6281.CouplingCriticalSpeedAnalysis):
    '''PartToPartShearCouplingCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCriticalSpeedAnalysis.TYPE'):
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
