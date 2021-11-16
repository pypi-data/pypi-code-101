'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._920 import SpiralBevelGearDesign
    from ._921 import SpiralBevelGearMeshDesign
    from ._922 import SpiralBevelGearSetDesign
    from ._923 import SpiralBevelMeshedGearDesign
