import re
from pathlib import Path


def replace(markdown: str, data: dict) -> str:
    for key in data:
        key_re = f"&shy;<!---\\s*{key}\\s*-->.*?<!---\\s*/{key}\\s*-->"
        key_str = f"&shy;<!---{key}-->{data[key]}<!---/{key}-->"
        markdown = re.sub(key_re, key_str, markdown)
    return markdown


def mark(filename: str, data: dict) -> bool:
    file = Path(filename)
    text = file.read_text()
    text = replace(text, data)
    file.write_text(text)
    return True
