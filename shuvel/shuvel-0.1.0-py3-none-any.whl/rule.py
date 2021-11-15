import enum
import json


class Severity(str, enum.Enum):
    HIGH = "high"
    LOW = "low"
    INFO = "info"


class Rule:
    def __init__(self, name: str, pattern: str, description: str, severity: Severity, references: list[str] = []):
        self.name = name
        self.pattern = pattern
        self.description = description
        self.severity = severity
        self.references = references

    def __repr__(self):
        return str(json.dumps(self.__dict__))
