"""Module to configure the Avahi package for service broadcast."""
import logging
from contextlib import contextmanager
from pathlib import Path

from foggy.exception import FoggyException

logging.getLogger(__name__).addHandler(logging.NullHandler())


class AvahiServiceBroadcastFailed(FoggyException):
    pass


SERVICE_FILE = Path("/etc/avahi/services/foggy.service")
XML = """<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">

<service-group>

  <name replace-wildcards="yes">%h</name>

  <service>
    <type>_foggy._tcp</type>
    <port>21210</port>
  </service>

</service-group>
"""


@contextmanager
def broadcast_service():
    try:
        logging.info("Starting service broadcast")
        SERVICE_FILE.write_text(XML)
        yield
    except FileNotFoundError as error:
        raise AvahiServiceBroadcastFailed(
            f"Could not write foggy avahi service to {SERVICE_FILE}"
        ) from error
    finally:
        logging.info("Stopping service broadcast")
        if SERVICE_FILE.exists():
            SERVICE_FILE.unlink()
