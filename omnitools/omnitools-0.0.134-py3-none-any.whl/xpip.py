from subprocess import call


_list = list


def pip(*args):
    call(["python3", "-m", "pip", *args])


def install(*args):
    pip("install", *args)


def uninstall(*args):
    pip("uninstall", *args)


def download(*args):
    pip("download", *args)


def freeze(*args):
    pip("freeze", *args)


def list(*args):
    pip("list", *args)


def show(*args):
    pip("show", *args)


def check(*args):
    pip("check", *args)


def config(*args):
    pip("config", *args)


def search(*args):
    pip("search", *args)


def cache(*args):
    pip("cache", *args)


def index(*args):
    pip("index", *args)


def wheel(*args):
    pip("wheel", *args)


def hash(*args):
    pip("hash", *args)


def completion(*args):
    pip("completion", *args)


def debug(*args):
    pip("debug", *args)


def help(*args):
    pip("help", *args)


