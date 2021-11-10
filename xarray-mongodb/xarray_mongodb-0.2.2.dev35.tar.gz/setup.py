#!/usr/bin/env python3
from setuptools import setup


def local_scheme(_):
    return ""


if __name__ == "__main__":
    setup(use_scm_version={"local_scheme": local_scheme})
