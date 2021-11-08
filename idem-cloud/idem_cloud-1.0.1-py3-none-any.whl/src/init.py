# Standard lib
import sys


def cli(hub):
    hub.pop.config.load(["idem", "acct"], cli="idem")
    hub.pop.loop.create()
    retcode = hub.pop.Loop.run_until_complete(hub.idem.init.cli_apply())
    sys.exit(retcode)
