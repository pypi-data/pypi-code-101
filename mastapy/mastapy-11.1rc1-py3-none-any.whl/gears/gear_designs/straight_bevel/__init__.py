'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._916 import StraightBevelGearDesign
    from ._917 import StraightBevelGearMeshDesign
    from ._918 import StraightBevelGearSetDesign
    from ._919 import StraightBevelMeshedGearDesign
