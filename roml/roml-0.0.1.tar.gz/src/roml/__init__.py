from .__version__ import __version__

def hello_world() -> None:
    print(
        "roml is a restrictive OpenML API and not meant as a replacement for `openml` Python."
        "Please use the `openml` package for interacting with OpenML for a tested and mature interface."
        "In fact, as of right now nothing has been implemented in roml."
    )
