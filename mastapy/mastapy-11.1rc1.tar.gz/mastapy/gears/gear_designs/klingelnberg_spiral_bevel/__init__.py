'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._924 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._925 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._926 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._927 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
