from typing import Dict, Optional, Type

from mdcode import Block

from dinject.executors.bash import BashExecutor
from dinject.executors.python import PythonExecutor
from dinject.types import Executor

executors: Dict[str, Type[Executor]] = {
    "bash": BashExecutor,
    "python": PythonExecutor,
}


def get_executor(block: Block) -> Optional[Executor]:
    """Gets an executor for `block`."""

    if t := executors.get(block.lang or "text", None):
        return t("\n".join(block.lines))
    return None
