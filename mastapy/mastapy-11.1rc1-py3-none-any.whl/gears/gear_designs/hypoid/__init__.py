'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._936 import HypoidGearDesign
    from ._937 import HypoidGearMeshDesign
    from ._938 import HypoidGearSetDesign
    from ._939 import HypoidMeshedGearDesign
