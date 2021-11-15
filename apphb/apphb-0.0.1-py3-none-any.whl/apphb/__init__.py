"""Application Heartbeats."""

from ._heartbeats import *

# The private _heartbeats namespace actually defines the core classes.
# We want these to appear as the top level (including in documentation).
HeartbeatFieldRecord.__module__ = __name__
HeartbeatRecord.__module__ = __name__
Heartbeat.__module__ = __name__
