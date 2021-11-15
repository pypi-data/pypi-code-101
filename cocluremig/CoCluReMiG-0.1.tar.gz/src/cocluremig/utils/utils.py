"""
Basic utilites
"""

import json


class JSONEncoder(json.JSONEncoder):
    """
    JSONEncoder which is more robust against some input data
    - replaces all iterables with lists
    """

    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, o)
