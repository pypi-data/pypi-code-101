from typing import List, Optional

import pydantic


class FunctionMetrics(pydantic.BaseModel):
    name: str
    depth: Optional[int] = None
    width: Optional[int] = None


class SynthesisMetrics(pydantic.BaseModel):
    duration_in_seconds: Optional[float] = None
    failure_reason: Optional[str] = None
    functions_metrics: Optional[List[FunctionMetrics]] = []
