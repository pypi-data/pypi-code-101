"""
    (c)2021 K. Goger (k.r.goger@gmail.com)
    legal: https://github.com/kr-g/mpymodcore/blob/master/LICENSE
"""

import os
import ubinascii

from modcore import modc, Module, LifeCycle, logger

from .wlan import wlan_ap, WLAN_CFG, WLAN_EV, WLAN_RESTART


NETWORK_CFG = "/etc/network/"

known_networks = {}


class NetworkManager(Module):
    def watching_events(self):
        return [
            WLAN_EV,
        ]

    def loop(self, config=None, event=None):
        if self.current_level() != LifeCycle.RUNNING:
            return

        if event != None:
            self.info("got event", event)

            if event.name == WLAN_EV:
                if event.get_data() == True:
                    info = wlan_ap.ifconfig()
                    self.info("connected to wlan", info)
                    self.network_add()
                    self.info("added network")

    # housekeeping

    def _build_file_name(self, mac):
        return mac + ".cfg"

    def network_add(self):
        """add current wlan.cfg file to known network list"""
        try:
            with open(WLAN_CFG) as f:
                cont = f.read()

            cfg = wlan_ap.parse_cfg(cont)
            mac = cfg["mac"]
            if len(mac) > 0:
                fnam = self._build_file_name(mac)
                with open(NETWORK_CFG + fnam, "wb") as f:
                    f.write(cont)

                global known_networks
                known_networks[mac] = cfg

            else:
                self.info(
                    "mac not configureed, dont save known network for ssid=",
                    cfg["ssid"],
                )

        except Exception as ex:
            self.excep(ex, "copy wlan cfg to known network list")

    def network_remove(self, mac):
        """remove wlan cfg file"""
        fnam = NETWORK_CFG + self._build_file_name(mac)
        try:
            os.remove(fnam)

            global known_networks
            del known_networks[mac]

        except Exception as ex:
            self.excep(ex, "remove wlan cfg", fnam)
            return ex

    def network_switch(self, mac, restart_wlan=True):
        """copy known network to current wlan cfg, and fire reconnect"""
        fnam = self._build_file_name(mac)
        try:
            with open(NETWORK_CFG + fnam) as f:
                cont = f.read()
            with open(WLAN_CFG, "wb") as f:
                f.write(cont)

        except Exception as ex:
            self.excep(ex, "copy wlan cfg", fnam)

        if restart_wlan == True:
            self.fire_event(WLAN_RESTART)

    def load_known_networks(self):
        global known_networks
        known_networks = {}
        try:
            cfg_files = filter(
                lambda x: x.lower().endswith(".cfg"), os.listdir(NETWORK_CFG)
            )
            for cfg in cfg_files:
                nam = cfg[0:-4]
                known_networks[nam] = cfg
                self.info("loaded netw", nam, cfg)

        except Exception as ex:
            self.excep(ex, "load_known_networks")


def ensure_network_folder():
    try:
        os.stat(NETWORK_CFG)
        return
    except Exception as ex:
        logger.info(ex, "not found", NETWORK_CFG)

    cwd = os.getcwd()

    try:
        subdirs = NETWORK_CFG.split("/")
        for p in subdirs:
            if len(p) > 0:
                try:
                    os.mkdir(p)
                    logger.info("created subdir", p)
                except:
                    logger.info("subdir exists", p)
                os.chdir(p)
        logger.info("created", NETWORK_CFG)

    except Exception as ex:
        logger.excep(ex, "create folder", NETWORK_CFG)

    os.chdir(cwd)


ensure_network_folder()

netw_man = NetworkManager("netwman")
netw_man.load_known_networks()

modc.add(netw_man)
