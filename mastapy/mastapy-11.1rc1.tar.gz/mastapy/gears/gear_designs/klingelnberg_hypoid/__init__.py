'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._928 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._929 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._930 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._931 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
