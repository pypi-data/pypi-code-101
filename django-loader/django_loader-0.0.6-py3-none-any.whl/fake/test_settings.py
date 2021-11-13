# ******************************************************************************
#
# django-loader, a configuration and secret loader for Django
#
# test_settings.py:  integration tests
#
# Copyright (C) 2021 Jeremy A Gray <gray@flyquackswim.com>.
#
# SPDX-License-Identifier: MIT
#
# ******************************************************************************
#
"""Integration tests."""

import sys

import pytest
from django.conf import settings

sys.path.insert(0, "/home/gray/src/work/django-loader")

import loader  # noqa: E402

# def test_load_allowed_hosts(monkeypatch):
#     """Should load ``ALLOWED_HOSTS``."""
#     monkeypatch.setenv("DJANGO_ENV_ALLOWED_HOSTS__0", "localhost")
#     monkeypatch.setenv("DJANGO_ENV_ALLOWED_HOSTS__1", "127.0.0.1")

#     actual = settings.ALLOWED_HOSTS
#     expected = [
#         "localhost",
#         "127.0.0.1",
#     ]

#     assert actual == expected
