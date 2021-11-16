'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._912 import StraightBevelDiffGearDesign
    from ._913 import StraightBevelDiffGearMeshDesign
    from ._914 import StraightBevelDiffGearSetDesign
    from ._915 import StraightBevelDiffMeshedGearDesign
