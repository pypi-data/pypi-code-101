'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2069 import ClutchConnection
    from ._2070 import ClutchSocket
    from ._2071 import ConceptCouplingConnection
    from ._2072 import ConceptCouplingSocket
    from ._2073 import CouplingConnection
    from ._2074 import CouplingSocket
    from ._2075 import PartToPartShearCouplingConnection
    from ._2076 import PartToPartShearCouplingSocket
    from ._2077 import SpringDamperConnection
    from ._2078 import SpringDamperSocket
    from ._2079 import TorqueConverterConnection
    from ._2080 import TorqueConverterPumpSocket
    from ._2081 import TorqueConverterTurbineSocket
