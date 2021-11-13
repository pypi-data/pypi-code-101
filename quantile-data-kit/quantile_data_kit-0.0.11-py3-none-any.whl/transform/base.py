from dagster import InputDefinition, OutputDefinition
from qdk.base import BaseComponent
from qdk.dagster_types import DataFrameType


class TransformComponent(BaseComponent):
    compute_function = "transform"
    tags = {
        "kind": "transform",
    }
    input_defs = [
        InputDefinition("df", DataFrameType),
    ]
    output_defs = [
        OutputDefinition(DataFrameType, "df"),
    ]

    @classmethod
    def transform(cls, df: DataFrameType, **config) -> DataFrameType:
        raise NotImplementedError(
            'Make sure you added a "transform" function to the component'
        )
