'''_2146.py

FELinkWithSelection
'''


from mastapy.system_model.fe.links import (
    _2144, _2145, _2147, _2148,
    _2149, _2150, _2151, _2152,
    _2153, _2154, _2155, _2156,
    _2157, _2158
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_LINK_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELinkWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FELinkWithSelection',)


class FELinkWithSelection(_0.APIBase):
    '''FELinkWithSelection

    This is a mastapy class.
    '''

    TYPE = _FE_LINK_WITH_SELECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FELinkWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def link(self) -> '_2144.FELink':
        '''FELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.FELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to FELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_electric_machine_stator_fe_link(self) -> '_2145.ElectricMachineStatorFELink':
        '''ElectricMachineStatorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.ElectricMachineStatorFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ElectricMachineStatorFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_gear_mesh_fe_link(self) -> '_2147.GearMeshFELink':
        '''GearMeshFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.GearMeshFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to GearMeshFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_gear_with_duplicated_meshes_fe_link(self) -> '_2148.GearWithDuplicatedMeshesFELink':
        '''GearWithDuplicatedMeshesFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.GearWithDuplicatedMeshesFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to GearWithDuplicatedMeshesFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_multi_angle_connection_fe_link(self) -> '_2149.MultiAngleConnectionFELink':
        '''MultiAngleConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2149.MultiAngleConnectionFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to MultiAngleConnectionFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_multi_node_connector_fe_link(self) -> '_2150.MultiNodeConnectorFELink':
        '''MultiNodeConnectorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2150.MultiNodeConnectorFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeConnectorFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_multi_node_fe_link(self) -> '_2151.MultiNodeFELink':
        '''MultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2151.MultiNodeFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_planetary_connector_multi_node_fe_link(self) -> '_2152.PlanetaryConnectorMultiNodeFELink':
        '''PlanetaryConnectorMultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2152.PlanetaryConnectorMultiNodeFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetaryConnectorMultiNodeFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_planet_based_fe_link(self) -> '_2153.PlanetBasedFELink':
        '''PlanetBasedFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2153.PlanetBasedFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetBasedFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_planet_carrier_fe_link(self) -> '_2154.PlanetCarrierFELink':
        '''PlanetCarrierFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2154.PlanetCarrierFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetCarrierFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_point_load_fe_link(self) -> '_2155.PointLoadFELink':
        '''PointLoadFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.PointLoadFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to PointLoadFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_rolling_ring_connection_fe_link(self) -> '_2156.RollingRingConnectionFELink':
        '''RollingRingConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.RollingRingConnectionFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to RollingRingConnectionFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_shaft_hub_connection_fe_link(self) -> '_2157.ShaftHubConnectionFELink':
        '''ShaftHubConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2157.ShaftHubConnectionFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ShaftHubConnectionFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    @property
    def link_of_type_single_node_fe_link(self) -> '_2158.SingleNodeFELink':
        '''SingleNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.SingleNodeFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to SingleNodeFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Link.__class__)(self.wrapped.Link) if self.wrapped.Link is not None else None

    def add_selected_nodes(self):
        ''' 'AddSelectedNodes' is the original name of this method.'''

        self.wrapped.AddSelectedNodes()

    def delete_all_nodes(self):
        ''' 'DeleteAllNodes' is the original name of this method.'''

        self.wrapped.DeleteAllNodes()

    def select_component(self):
        ''' 'SelectComponent' is the original name of this method.'''

        self.wrapped.SelectComponent()
