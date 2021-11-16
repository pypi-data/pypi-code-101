'''_5089.py

AbstractShaftOrHousingMultibodyDynamicsAnalysis
'''


from mastapy._internal import constructor
from mastapy.system_model.part_model import _2164, _2163, _2179
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2208
from mastapy.system_model.part_model.cycloidal import _2294
from mastapy.system_model.analyses_and_results.mbd_analyses import _5115
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AbstractShaftOrHousingMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingMultibodyDynamicsAnalysis',)


class AbstractShaftOrHousingMultibodyDynamicsAnalysis(_5115.ComponentMultibodyDynamicsAnalysis):
    '''AbstractShaftOrHousingMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_rigid_body_degrees_of_freedom(self) -> 'int':
        '''int: 'NumberOfRigidBodyDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfRigidBodyDegreesOfFreedom

    @property
    def component_design(self) -> '_2164.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.AbstractShaftOrHousing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_abstract_shaft(self) -> '_2163.AbstractShaft':
        '''AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.AbstractShaft.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_fe_part(self) -> '_2179.FEPart':
        '''FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.FEPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FEPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2208.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.Shaft.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2294.CycloidalDisc':
        '''CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2294.CycloidalDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
