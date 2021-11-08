from acct.conf import CLI_CONFIG as ACCT_CLI_CONFIG
from idem.conf import CLI_CONFIG as IDEM_CLI_CONFIG


# Merge Idem and ACCT CLI here
CLI_CONFIG = {}
CLI_CONFIG.update(ACCT_CLI_CONFIG)
CLI_CONFIG.update(IDEM_CLI_CONFIG)


GLOBAL = {}
SUBS = {}
DYNE = {"idem_cloud": ["src"]}
