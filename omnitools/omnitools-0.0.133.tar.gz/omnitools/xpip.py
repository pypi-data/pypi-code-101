import pip


_list = list


def PIP(*args):
    if hasattr(pip, "main"):
        pip.main(_list(args))
    else:
        pip._internal.main(_list(args))


def install(*args):
    PIP("install", *args)


def uninstall(*args):
    PIP("uninstall", *args)


def download(*args):
    PIP("download", *args)


def freeze(*args):
    PIP("freeze", *args)


def list(*args):
    PIP("list", *args)


def show(*args):
    PIP("show", *args)


def check(*args):
    PIP("check", *args)


def config(*args):
    PIP("config", *args)


def search(*args):
    PIP("search", *args)


def cache(*args):
    PIP("cache", *args)


def index(*args):
    PIP("index", *args)


def wheel(*args):
    PIP("wheel", *args)


def hash(*args):
    PIP("hash", *args)


def completion(*args):
    PIP("completion", *args)


def debug(*args):
    PIP("debug", *args)


def help(*args):
    PIP("help", *args)


