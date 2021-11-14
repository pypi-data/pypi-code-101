import os
import sys
import re
from pathlib import Path
from typing import Tuple, List


def get_existing_themes(regex: re.Pattern, content: str) -> Tuple[List[str], bool]:
    m = regex.search(content)
    if not m:  # no section
        return [], False
    elif not m.group(1):  # no themes but empty section exists
        return [], True

    return [x.strip() for x in m.group(1).split(" ")], True


def build_new_zshrc_content(new_ignored_theme_name: str, zshrc_content: str) -> str:

    regex = re.compile(
        r"^ZSH_THEME_RANDOM_IGNORED=\(\s*((?:\w+\s*)+)?\)$", re.MULTILINE
    )
    ignored_theme_names, section_exists = get_existing_themes(regex, zshrc_content)
    ignored_theme_names.append(new_ignored_theme_name)

    new_line = (
        f"ZSH_THEME_RANDOM_IGNORED=({' '.join(sorted(ignored_theme_names)).strip()})"
    )

    if section_exists:
        return regex.sub(new_line, zshrc_content)
    else:
        return f"{zshrc_content}\n{new_line}\n"


def main():
    assert len(sys.argv) == 2, "Usage: main.py <theme_name>"
    random_theme = sys.argv[1]
    assert re.match("^[a-zA-Z0-9_]+$", random_theme), "Theme name must be alphanumeric"

    zshrc_path = Path(os.path.expanduser("~/.zshrc"))
    zshrc_path.write_text(build_new_zshrc_content(random_theme, zshrc_path.read_text()))


if __name__ == "__main__":
    main()
