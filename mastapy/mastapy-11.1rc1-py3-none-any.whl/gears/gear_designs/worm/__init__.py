'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._907 import WormDesign
    from ._908 import WormGearDesign
    from ._909 import WormGearMeshDesign
    from ._910 import WormGearSetDesign
    from ._911 import WormWheelDesign
