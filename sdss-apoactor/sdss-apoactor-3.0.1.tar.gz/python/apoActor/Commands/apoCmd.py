#!/usr/bin/env python

import os
from time import sleep

from opscore.utility.qstr import qstr

from apoActor.wx import WX


class apoCmd(object):
    """Wrap commands to the apo actor"""

    def __init__(self, actor):
        self.actor = actor

        # Declare commands

        self.vocab = [
            ("ping", "", self.ping),
            ("status", "", self.status),
            ("update", "", self.update),
        ]

    def ping(self, cmd):
        """Query the actor for liveness/happiness."""

        cmd.finish("text='Present and (probably) correct'")

    def status(self, cmd):
        """Report status and version; obtain and send current data"""

        self.actor.sendVersionKey(cmd)
        self.doStatus(cmd, flushCache=True)

    def update(self, cmd):
        """Report status and version; obtain and send current data"""

        self.doStatus(cmd=cmd)

    def doStatus(self, cmd=None, flushCache=False):
        """Obtain data and send it to the hub and optionally the TCC"""

        if not cmd:
            cmd = self.actor.bcast

        #
        # Flush the data cache if requested (all data, not just updated data)
        #
        if flushCache:
            self.actor.cachedValues = {}

        w = WX().recvcat("tuples", dict=True)

        #
        # Check for OK reply
        #
        while w.v.recv_status != "OK":
            w = WX().recvcat("tuples", dict=True)
            if w.v.recv_status != "OK":
                cmd.warn('recv_status="%s"' % w.v.recv_status)
                sleep(1)

        #
        # Retrieve file system information
        #
        fsdict = {}
        for volume in self.actor.fsvolumes:
            fsinfo = os.statvfs(volume)
            fssize = fsinfo.f_frsize * fsinfo.f_blocks
            fsfree = fsinfo.f_frsize * fsinfo.f_bavail
            fsdict[volume] = (fssize, fsfree)

        # cmd.debug('text="fsvolumes: %s"' % fsdict)

        #
        # Send updated values to tron
        #
        updated = 0
        new = 0
        keyStrings = []
        for key in self.actor.kdict.keys.values():
            name = key.name
            #
            # Check if key is present in data dictionary
            #
            if name in w.v.d:
                msg = "%s=%s" % (name, w.v.d[name][1])
                #
                # Check for previous presence of key
                #
                if name in self.actor.cachedValues:
                    #
                    # Check for change of timestamp and value
                    #
                    if w.v.d[name] != self.actor.cachedValues[name]:
                        keyStrings.append(msg)
                        updated += 1
                else:
                    keyStrings.append(msg)
                    new += 1

        #
        # Seperately generate disk space keywords for each volume
        #
        for host in self.actor.fshost:
            oneGig = 1024 * 1024 * 1024.0
            for volume in self.actor.fsvolumes:
                ratio = fsdict[volume][1] / fsdict[volume][0]
                msg = "diskspace=%s,%s,%d,%d" % (
                    qstr(host),
                    qstr(volume),
                    fsdict[volume][0] / oneGig,
                    fsdict[volume][1] / oneGig,
                )
                if ratio <= 0.1:
                    cmd.warn(msg)
                else:
                    cmd.inform(msg)

        keyMsg = "; ".join(keyStrings)
        self.actor.logger.info(
            "%d %d %s" % (new, updated, keyMsg if keyMsg else "no updated wx data")
        )

        #
        # Send weather data to TCC if requested
        #
        # The TCC uses pressure in Pascals and humidity as a fraction of one
        # so we convert from inHg -> Pascals and % -> fraction respectively.
        #
        # Note that the TCC only accepts strings up to 132 characters.
        #
        if int(self.actor.config["apo"]["sendToTCC"]):
            new = 0
            tccStrings = []
            for name in self.actor.tccNameDict.keys():
                #
                # Check if key is present in data dictionary
                #
                if name in w.v.d:
                    new += 1
                    #
                    # Get the TCC's name for this key
                    #
                    tccName = self.actor.tccNameDict[name]
                    #
                    # Handle unit conversions
                    #
                    if name == "pressure":
                        tccStrings.append(
                            "%s=%.3f"
                            % (tccName, 3386.3788 * float(w.v.d["pressure"][1]))
                        )
                    elif name == "humidPT":
                        tccStrings.append(
                            "%s=%.3f" % (tccName, 0.01 * float(w.v.d["humidPT"][1]))
                        )
                    else:
                        tccStrings.append("%s=%s" % (tccName, w.v.d[name][1]))

            tccMsg = "set weather " + ", ".join(tccStrings)
            self.actor.logger.info("%d %s" % (new, tccMsg))

            cmdVar = self.actor.cmdr.call(actor="tcc", cmdStr=tccMsg, timeLim=3.0)
            if cmdVar.didFail:
                cmd.error("text='Failed to set TCC weather'")

        # Store data to use in check for updated data on the next call
        #
        self.actor.cachedValues = w.v.d
        #
        # Finish and send data message to hub
        #
        cmd.finish(keyMsg)
