'''_2532.py

SpringDamperSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2325
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6662
from mastapy.system_model.analyses_and_results.power_flows import _3857
from mastapy.system_model.analyses_and_results.system_deflections import _2451
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SpringDamperSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperSystemDeflection',)


class SpringDamperSystemDeflection(_2451.CouplingSystemDeflection):
    '''SpringDamperSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperSystemDeflection.TYPE'):
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

    @property
    def power_flow_results(self) -> '_3857.SpringDamperPowerFlow':
        '''SpringDamperPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3857.SpringDamperPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
