#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys


def create_readme():
    """Create a README for the new project"""
    proj_name = sys.argv[2]
    proj_path = Path(proj_name)
    readme_path = proj_path / "README.md"
    with readme_path.open("w+", encoding="utf-8") as readme:
        readme.write(f"# {proj_name}\n\n")
        readme.seek(0)


if __name__ == "__main__":
    create_readme()
