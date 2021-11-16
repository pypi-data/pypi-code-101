import uuid


class Event:
    """
    A model class to define Event
    """
    def __init__(self, type_: str, message: str):
        self.id_ = str(uuid.uuid4())
        self.type_ = type_
        self.message = message

    def __str__(self):
        return f'Event(id={self.id_})'
