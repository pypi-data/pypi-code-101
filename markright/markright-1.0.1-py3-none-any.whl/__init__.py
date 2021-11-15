import re
from pathlib import Path


def clean(markdown: str) -> str:
    pattern = r"&shy;<!---\s*(.+)\s*-->.*?<!---\s*/\1\s*-->"
    markdown = re.sub(pattern, r"&shy;<!---\1--><!---/\1-->", markdown)
    return markdown


def replace(markdown: str, data: dict) -> str:
    for key in data:
        pattern = f"&shy;<!---\\s*{key}\\s*-->.*?<!---\\s*/{key}\\s*-->"
        replacer = f"&shy;<!---{key}-->{data[key]}<!---/{key}-->"
        markdown = re.sub(pattern, replacer, markdown)
    return markdown


def mark(filename: str, data: dict) -> bool:
    file = Path(filename)
    text = file.read_text()
    text = clean(text)
    text = replace(text, data)
    file.write_text(text)
    return True
