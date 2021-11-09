import typing as t
from fnmatch import fnmatch

from fw_utils import Tokenizer


# Adapted from Flyhweel, xfer library
# https://gitlab.com/flywheel-io/tools/app/xfer/-/blob/master/xfer/exports/templates.py
def parse_expression(expr: str) -> t.Iterable[t.Tuple[str, str]]:
    """Parse template expression."""
    tokens = Tokenizer(expr)
    field = fmt = ""
    read_fmt = False
    for token in tokens:
        if token == ":":
            if not field:
                raise ValueError("unexpected char :, expected a field")
            read_fmt = True
        elif token == "|":
            if not field:
                raise ValueError("unexpected char |, expected a field")
            yield field, fmt
            field = fmt = ""
            read_fmt = False
        elif read_fmt:
            fmt += token
        else:
            field += token
    if not field:
        raise ValueError("unexpected end of expression")
    yield field, fmt


def validate_path(path: str, valid_fields: t.List[str]) -> str:
    """Validate and canonize export template path."""

    def validate_field(field: str):
        if not any(fnmatch(field, f) for f in valid_fields):
            raise ValueError(f"unexpected field: {field}")

    tokens = Tokenizer(path)
    result = ""
    for token in tokens:
        if token in ("\\{", "\\}"):
            result += token[1]
        elif token == "{":
            result += token
            expr = tokens.get_until("}")
            parsed = []
            for field, fmt in parse_expression(expr):
                validate_field(field)
                if fmt and not field.endswith("timestamp"):
                    raise ValueError("only timestamp fields can be formatted")
                if fmt:
                    parsed.append(f"{field}:{fmt}")
                else:
                    parsed.append(field)
            result += "|".join(parsed)
            result += "}"
        else:
            result += token
    return result
