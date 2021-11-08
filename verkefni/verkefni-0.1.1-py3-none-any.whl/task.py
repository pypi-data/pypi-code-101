from dataclasses import dataclass


@dataclass
class Task:
    id: str
    function: str = None
    input_data: any = None
