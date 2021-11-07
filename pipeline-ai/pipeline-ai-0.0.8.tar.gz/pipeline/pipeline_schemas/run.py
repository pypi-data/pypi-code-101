from enum import Enum
import datetime
from typing import List, Optional, Union

from pydantic import Field, validator

from .base import BaseModel
from .data import DataGet
from .runnable import (
    FunctionGet,
    FunctionDetailedGet,
    RunnableIOGet,
    PipelineGet,
    PipelineDetailedGet,
)
from .tag import Tag
from .token import Token


class RunState(Enum):
    RECEIVED = "received"
    ALLOCATING_CLUSTER = "allocating_cluster"
    ALLOCATING_RESOURCE = "allocating_resource"
    LOADING_DATA = "loading_data"
    LOADING_FUNCTION = "loading_function"
    LOADING_PIPELINE = "loading_pipeline"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"


class RunCreateSchema(BaseModel):
    # id: Optional[str]
    # token: Optional[str]
    pipeline_id: Optional[str]
    function_id: Optional[str]
    data: Optional[str]
    data_id: Optional[str]

    class Config:
        orm_mode = True

    @validator("pipeline_id")
    def validate_pipeline(cls, value, **kwargs):
        return value

    @validator("function_id")
    def validate_function(cls, value, **kwargs):
        if (
            "values" in kwargs
            and "pipeline_id" in kwargs["values"]
            and kwargs["values"]["pipeline_id"] != None
        ):
            raise ValueError("Can only pass in function_id or pipeline_id, not both.")
        elif value == None:
            raise ValueError("Must pass in function_id or pipeline_id")
        return value

    @validator("data")
    def validate_data(cls, value, **kwargs):
        return value

    @validator("data_id")
    def validate_data_id(cls, value, **kwargs):
        if (
            "values" in kwargs
            and "data" in kwargs["values"]
            and kwargs["values"]["data"] != None
        ):
            raise ValueError("Can only pass in data or data_id, not both.")
        elif value == None:
            raise ValueError("Must pass in data or data_id")
        return value


class RunIOGet(RunnableIOGet):
    """Realised/given input/output data to a Runnable used in a Run."""

    value: str
    data_url: str


class RunGet(BaseModel):
    id: str
    created_at: datetime.datetime
    started_at: Optional[datetime.datetime]
    ended_at: Optional[datetime.datetime]
    status: RunState = Field(..., alias="run_state")
    compute_time_ms: Optional[int]
    runnable: Union[FunctionGet, PipelineGet]
    # token: str
    data: DataGet
    blocking: Optional[bool] = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RunDetailedGet(RunGet):
    runnable: Union[FunctionDetailedGet, PipelineDetailedGet]
    n_resources: int
    resource_type: str
    region: str
    tags: List[Tag] = []
    inputs: List[RunIOGet] = []
    outputs: List[RunIOGet] = []
    token: Token


class RunOnResourceSchema(RunGet):
    resource_id: str

    class Config:
        orm_mode = True


"""
class RunCreateSchema(RunSchema):
    token: str
    run_target_type: RunTypeEnum


class RunFunction(BaseModel):
    id: str
    token: str
    function: FunctionGet
"""
