from .version import __version__  # noqa: F401
from .ipyslurm import IPySlurm  # noqa: I100
from .slurm import Slurm  # noqa: F401


def load_ipython_extension(ipython):
    ipython.register_magics(IPySlurm)
