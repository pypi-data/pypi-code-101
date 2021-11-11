from functools import wraps
from flask import g


def app_loaded_required(view):
    """ Validates that a PAB app is loaded. """
    @wraps(view)
    def wrapped(**kwargs):
        if not g.app:
            return "APP_NOT_LOADED", 500
        return view(**kwargs)
    return wrapped
