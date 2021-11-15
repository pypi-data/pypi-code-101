import dataclasses
import distutils.util
import os
from io import StringIO
from typing import List

from dotenv import dotenv_values


def from_string(schema: dataclasses.dataclass, env_str: str) -> dataclasses.dataclass:
    env_values = dotenv_values(stream=StringIO(env_str))
    return parse_dataclass(schema, env_values)


def from_file(schema: dataclasses.dataclass, env_path: str) -> dataclasses.dataclass:
    if not os.path.exists(env_path):
        raise FileNotFoundError(f'.env file does not exist at provided path ({env_path})')
    env_values = dotenv_values(dotenv_path=env_path)
    return parse_dataclass(schema, env_values)


def get_schema_fields(schema: dataclasses.dataclass) -> List[dataclasses.Field]:
    output: List[dataclasses.Field] = []
    for a, b in vars(schema).items():
        if a == '__dataclass_fields__':
            for key in b:
                output.append(b[key])
    return output


def get_missing_fields(schema_fields: List[dataclasses.Field], env_values: dict) -> List[str]:
    flat_schema_fields = set(map(lambda x: x.name, schema_fields))
    flat_env_values = set(map(lambda x: x[0], env_values))
    return list(flat_schema_fields - flat_env_values)


def parse_dataclass(schema: dataclasses.dataclass, env_values: dict) -> dataclasses.dataclass:
    schema_fields: List[dataclasses.Field] = get_schema_fields(schema)
    export = {}
    for field in schema_fields:
        if field.name in env_values:
            value: str = env_values[field.name]
            try:
                if field.type is bool:
                    export[field.name] = bool(distutils.util.strtobool(value))
                elif field.type is int:
                    export[field.name] = int(value)
                elif field.type is List[int]:
                    export[field.name] = [int(k) for k in value.split(',')]
                elif field.type is List[str]:
                    export[field.name] = [k.strip() for k in value.split(',')]
                else:
                    export[field.name] = value
            except ValueError:
                pass
    try:
        return schema(**export)
    except TypeError:
        missing_fields = ', '.join(get_missing_fields(schema_fields, env_values))
        raise ValueError(f'Schema is missing required fields: {missing_fields}')
