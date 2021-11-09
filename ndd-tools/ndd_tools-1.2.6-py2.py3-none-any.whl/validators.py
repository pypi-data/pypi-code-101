


def check_instance_of(obj, obj_type, allow_none=False):
    if obj is None and allow_none:
        return

    if not isinstance(obj, obj_type):
        raise TypeError(f'expect {obj!r} is an instance of {obj_type!r}')
    