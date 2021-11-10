from subprocess import Popen


def pip(*args):
    args = ["python3", "-m", "pip", *args]
    print(" ".join(args))
    return Popen(args).communicate()


def install(*args):
    return pip("install", *args)


def uninstall(*args):
    return pip("uninstall", *args)


def download(*args):
    return pip("download", *args)


def freeze(*args):
    return pip("freeze", *args)


def list(*args):
    return pip("list", *args)


def show(*args):
    return pip("show", *args)


def check(*args):
    return pip("check", *args)


def config(*args):
    return pip("config", *args)


def search(*args):
    return pip("search", *args)


def cache(*args):
    return pip("cache", *args)


def index(*args):
    return pip("index", *args)


def wheel(*args):
    return pip("wheel", *args)


def hash(*args):
    return pip("hash", *args)


def completion(*args):
    return pip("completion", *args)


def debug(*args):
    return pip("debug", *args)


def help(*args):
    return pip("help", *args)


