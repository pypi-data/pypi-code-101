__version__ = "3.1.6"
__description__ = "One-stop solution for HTTP(S) testing."

# import firstly for monkey patch if needed
from viper_hrunner.vhrun.ext.locust import main_locusts
from viper_hrunner.vhrun.parser import parse_parameters as Parameters
from viper_hrunner.vhrun.runner import HttpRunner
from viper_hrunner.vhrun.testcase import Config, Step, RunRequest, RunTestCase

__all__ = [
    "__version__",
    "__description__",
    "HttpRunner",
    "Config",
    "Step",
    "RunRequest",
    "RunTestCase",
    "Parameters",
]
