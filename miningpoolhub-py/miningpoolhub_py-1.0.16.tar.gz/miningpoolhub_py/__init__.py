import os
from dotenv import load_dotenv
import pkg_resources

load_dotenv()

__version__ = pkg_resources.get_distribution("miningpoolhub_py").version
__author__ = "Cory Krol"

API_KEY = os.environ.get("MPH_API_KEY", None)

from .miningpoolhubapi import MiningPoolHubAPI

# TODO: Possible Errors
# 1. Bad auth token -> 401 Unauthorized ('Access denied')
# 2. Success status on auto switching bad -> APIError
# 4. API Key Rate limit error
# 5. Need to test calls to API for new account with 0s/nulls in responses -> 200, html document as response
