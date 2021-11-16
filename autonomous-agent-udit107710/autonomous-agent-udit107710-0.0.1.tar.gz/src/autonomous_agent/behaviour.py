from typing import Dict, Optional, Any, Mapping
import uuid


class Behaviour:
    """
    A model class to define Behaviours
    """
    def __init__(self, condition, message_type: str, message_text: str, globals_: Optional[Dict[str, Any]] = None, locals_: Optional[Mapping[str, Any]]= None):
        self.condition = condition
        self.locals_: Optional[Mapping[str, Any]] = locals_
        self.globals_: Optional[Dict[str, Any]] = globals_
        self.message_text: str = message_text
        self.message_type: str = message_type
        self.id_: str = str(uuid.uuid4())
    
    def __str__(self):
        return f'Behaviour(id={self.id_})'
