import pydatfile.files
import pydatfile.coders
import pydatfile.errors


def encode(data):
    return pydatfile.coders.encode(data)


def decode(data):
    return pydatfile.coders.decode(data)


def open(path, except_value=pydatfile.errors.NotSet):
    return pydatfile.files.File(path, ensure_with=except_value)


def create(path, data, hold_readable):
    f = pydatfile.files.File(path, True)
    f.write(data, force_human_readable=hold_readable)
    return f
