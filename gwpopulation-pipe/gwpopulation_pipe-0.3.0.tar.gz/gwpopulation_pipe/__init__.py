try:
    import os

    with open(os.path.join(os.path.dirname(__file__), ".version"), "r") as ff:
        __version__ = ff.readline()
except FileNotFoundError:
    import warnings

    warnings.warn("gwpopulation_pipe version file not found.")
    __version__ = ""
