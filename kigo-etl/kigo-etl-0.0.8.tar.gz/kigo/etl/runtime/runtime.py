import os.path

from kigo.etl.storage.memdb import MemoryDB
from kigo.etl.runtime.registry import MappingRegistry


class MetaReflection:
    OPERATIONS = {}

    @classmethod
    def operations(cls, clazz):
        if clazz in MetaReflection.OPERATIONS:
            return MetaReflection.OPERATIONS[clazz]
        else:
            MetaReflection.OPERATIONS[clazz] = {}

        for field, oper in clazz.__dict__.items():
            if not field.startswith("__"):
                MetaReflection.OPERATIONS[clazz][field] = oper
        return MetaReflection.OPERATIONS[clazz]


class ExtractData:

    @classmethod
    def extract(cls, clazz, num, data) -> dict:
        unit = {}
        for field, operation in MetaReflection.operations(clazz).items():
            unit[field] = operation.call(num, data, unit)
        return unit


def check_readers():
    non_existing_file = []
    for mapp in MappingRegistry.mappings:
        for init_reader in MappingRegistry.mappings[mapp].readers:
            typeof_reader, init = init_reader
            if not os.path.exists(init["path"]):
                non_existing_file.append(init['path'])
    return non_existing_file


def process_mapping():
    non_existing_file = check_readers()
    print(f"non-existing files: {non_existing_file}")
    db = MemoryDB()
    for mapp in MappingRegistry.mappings:
        for init_reader in MappingRegistry.mappings[mapp].readers:
            typeof_reader, init = init_reader
            if init["path"] in non_existing_file:
                continue
            r = typeof_reader(**init)
            for line in r:
                data = ExtractData.extract(MappingRegistry.mappings[mapp].clazz[0], *line)
                db.store(MappingRegistry.mappings[mapp].clazz[0], data)
    return db


def process()->MemoryDB:
    db = process_mapping()
    return db
