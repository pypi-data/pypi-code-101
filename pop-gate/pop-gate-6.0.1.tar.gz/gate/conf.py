CLI_CONFIG = {
    "host": {"group": "Gate"},
    "port": {"group": "Gate"},
    "server": {"group": "Gate"},
    "prefix": {"group": "Gate"},
    "matcher": {"group": "Gate"},
    "refs": {"group": "Gate"},
    "limit_concurrency": {"group": "Gate"},
}
CONFIG = {
    "host": {
        "default": "0.0.0.0",
        "type": str,
        "help": "The host interface to bind to.",
    },
    "port": {"default": 8080, "type": int, "help": "The port to bind to"},
    "limit_concurrency": {
        "default": None,
        "type": int,
        "help": "The Maximum number of concurrent connections or tasks to allow, before issuing HTTP 503 responses.  "
        "This is useful for ensuring known memory usage patterns even under over-resourced loads.",
    },
    "server": {"default": "starlette", "help": "The server plugin interface to use"},
    "prefix": {
        "default": None,
        "type": str,
        "help": "The prefix for hub references that can be exposed",
    },
    "matcher": {
        "default": "glob",
        "type": str,
        "help": "The matcher plugin that will be used on the refs",
    },
    "refs": {
        "default": ["gate.init.test"],
        "help": "The hub references to expose",
        "nargs": "*",
    },
}
SUBCOMMANDS = {}
DYNE = {
    "gate": ["gate"],
    "matcher": ["matcher"],
    "srv": ["srv"],
}
