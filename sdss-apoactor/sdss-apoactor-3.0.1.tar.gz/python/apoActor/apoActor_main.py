#!/usr/bin/env python
"""An actor to process APO status messages and send them to the hub"""

from twisted.internet import reactor

import actorcore.Actor
import actorcore.CmdrConnection

from apoActor import __version__


class APO(actorcore.Actor.Actor):
    def __init__(self, name, productName=None, configFile=None, debugLevel=30):
        actorcore.Actor.Actor.__init__(
            self,
            name,
            productName=productName,
            configFile=configFile,
        )

        self.version = __version__

        self.logger.setLevel(debugLevel)
        self.logger.propagate = True

        #
        # Get filesystems for diskspace check in apoCmd.doStatus
        #
        self.fshost = self.config["diskspace"]["fshost"].split(",")
        self.fsvolumes = self.config["diskspace"]["fsvolumes"].split(",")

        #
        # Get the keys for use in apoCmd.doStatus
        #
        import opscore.protocols.keys as protoKeys

        self.kdict = protoKeys.KeysDictionary.load(name)
        #
        # Get the dictionary for use in talking to the TCC
        #
        self.tccNameDict = {
            "truss25m": "sectrusstemp",
            "airTempPT": "airtemp",
            "winds": "wspeed",
            "windd": "wdir",
            "pressure": "pressure",
            "humidPT": "humid",
        }

        # Initialize the data cache, for use in apoCmd.doStatus
        #
        self.cachedValues = {}

        # Schedule an update.
        #
        self.statusTimer = reactor.callLater(
            int(self.config[self.name]["updateInterval"]),
            self.periodicStatus,
        )
        # Finally start the reactor
        #
        self.run()

    def periodicStatus(self):
        """Run 'apoCmd.doStatus' periodically"""
        #
        # Obtain and send the data
        #
        self.callCommand("update")
        self.statusTimer = reactor.callLater(
            int(self.config[self.name]["updateInterval"]),
            self.periodicStatus,
        )


# To work
if __name__ == "__main__":
    apo = APO("apo", "apoActor", debugLevel=15)
