# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""context.py
Context helper functions.
"""

from flask import current_app, session
import os
from sweetrpg_web_core import constants


def get_context() -> dict:
    return {
        'user': {
            'id': session.get(constants.SESSION_EMAIL),
            'email': session.get(constants.SESSION_USER_ID),
        },
        'base_path': os.environ.get(constants.APPLICATION_BASE_PATH, ""),
        'static_asset_prefix': os.environ.get(constants.STATIC_ASSET_PREFIX, "")
    }
