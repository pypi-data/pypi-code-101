'''_2439.py

ConceptCouplingSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2306
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6539
from mastapy.system_model.analyses_and_results.power_flows import _3778
from mastapy.system_model.analyses_and_results.system_deflections import _2451
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptCouplingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingSystemDeflection',)


class ConceptCouplingSystemDeflection(_2451.CouplingSystemDeflection):
    '''ConceptCouplingSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2306.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2306.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6539.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6539.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3778.ConceptCouplingPowerFlow':
        '''ConceptCouplingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3778.ConceptCouplingPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
