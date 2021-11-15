import json
from hashlib import md5

from vtb_django_utils.model_versions.utils.json import JSONEncoder


def get_json_hash(json_obj):
    return md5(json.dumps(json_obj, sort_keys=True, cls=JSONEncoder).encode()).hexdigest()
