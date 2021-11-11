import typing as t
from fnmatch import fnmatch
from pathlib import Path

AnyPath = t.Union[str, Path]


# Adapted from Flyhweel, xfer library
# https://gitlab.com/flywheel-io/tools/app/xfer/-/blob/master/xfer/exports/templates.py
class Tokenizer:
    # TODO: sunset when support for python 3.7 is deprecated in favor of fw_utils
    """Simple tokenizer to help parsing patterns."""

    def __init__(self, string: str):
        """Tokenize the given string."""
        self.string = string
        self.index = 0
        self.char: t.Optional[str] = None

    def __iter__(self) -> "Tokenizer":
        """Return tokenizer itself as an iterator."""
        return self

    def __next__(self) -> str:
        """Get the next char or 2 chars if it's escaped."""
        index = self.index
        try:
            char = self.string[index]
        except IndexError as exc:
            raise StopIteration from exc

        if char == "\\":
            index += 1
            try:
                char += self.string[index]
            except IndexError as exc:
                raise ValueError("Pattern ending with backslash") from exc

        self.index = index + 1
        self.char = char
        return char

    def get_until(self, terminals: t.Optional[str] = None) -> str:
        """Get until terminal character or until the end if no terminals specified."""
        result = ""
        for char in self:
            if terminals and char in terminals:
                break
            result += char
        else:
            if terminals:
                raise ValueError(f"missing {terminals}, unterminated pattern")
        return result


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


# def download_file_core_client(api_key, file_id, dst_file):
#     from fw_core_client import CoreClient
#
#     core_client = CoreClient(
#         api_key=api_key, client_name="temporary", client_version="0.0.0"
#     )
#     if not Path(dst_file).parent.exists():
#         Path(dst_file).parent.mkdir(parents=True)
#     with open(dst_file, "wb") as writer:
#         resp = core_client.get(f"/files/{file_id}/download?ticket", stream=True)
#         writer.write(resp.content)


def download_file_with_sdk(api_key, file_id, dst_file):
    # TODO: sunset when support for python 3.7 is dropped
    import flywheel

    client = flywheel.Client(api_key)
    if not Path(dst_file).parent.exists():
        Path(dst_file).parent.mkdir(parents=True)
    file = client.get_file(file_id)
    acq = client.get(file.parents.acquisition)
    acq.download_file(file.name, dst_file)
    client.shutdown()
