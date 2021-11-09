import threading
import ipaddress
import re
import time
import socket
import os


class Monitor:
    """A dead hand system that monitor changes in network device and act accordingly."""

    def __init__(self, method, target, interval, callback, *args, retry=0,
        offline=True, all=True, delay=None, **kwargs):
        """Init the monitor with appropriate parameters. Currently support
        monitor device status with IP address and MAC address. Require the
        target device to be within same network.

        Parameters
        ----------
        method : str
            Takes "IP" or "MAC" as values. Used to specifies the ways to probe
            target devices. Must match the type of `target` parameter. Currently
            only check by IP address is supported.

        target : str || [str]
            The IP or MAC address of the target device(s). Must match the type
            of `method` parameter. If multiple target passed in, then all of
            them will be checked.

        interval : int
            The number of seconds until next check.

        callback : callable
            The callback function when device status change meets the required
            criteria. Will be called with `args` and `kwargs`.

        retry : int, optional
            Number of times to retry with `interval` apart until the system
            is considered triggered. Default is no retry.

        offline : bool, optional
            Triggers the callback function when device went offline or online.
            Default to when device went offline.

        all : bool, optional
            Used when multiple targets are passed in. If true, then all targets
            need to meet criteria before system triggered. Else, only one device
            status is required. Default to True.

        delay : int, optional
            The number of seconds delay of execute callback after triggered.
            Default is None.

        *args : arguments
            Used for callback function.

        **kwargs : keyword arguments
            Used for callback function.

        Raises
        ------
        ValueError
            When method provided is incorrect, or target provided mismatch
            with the method.
        """

        self.child = None
        self.changeTarget(method, target)

        self.interval = interval
        self.callback = callback
        self.retry = retry
        self.offline = offline
        self.testAll = all
        self.delay = delay
        self.args = args
        self.kwargs = kwargs
        self.__quit = False

    def activate(self):
        """Activates the Perimetr system"""
        if self.child is None or not self.child.is_alive():
            if self.method == "IP":
                self.child = threading.Thread(target=self.__ipCheck)
            elif self.method == "MAC":
                self.child = threading.Thread(target=self.__macCheck)

            self.__quit = False
            self.child.start()

    def deactivate(self, wait=False):
        """Deactivates the Perimetr system before the next scheduled check

        Parameters
        ----------
        wait : bool, optional
            Waits for the monitor system to be dearmed. May take as long as
            the entire `interval`. Default to False.
        """
        if self.child is not None and self.child.is_alive():
            self.__quit = True
            if wait:
                self.child.join()

    def changeTarget(self, method, target, force=False):
        """Changes the designated monitor method and target

        Parameters
        ----------
        method : str
            Takes "IP" or "MAC" as values. Used to specifies the ways to probe
            target devices. Must match the type of `target` parameter.

        target : str || [str]
            The IP or MAC address of the target device(s). Must match the type
            of `method` parameter. If multiple target passed in, then all of
            them will be checked.

        force : bool, optional
            Deactivate the system and then change the target if the system is
            running. May take longer to wait for deactivation. Will reinstate
            the monitor sequence after target change complete.
        """
        restart = False
        if self.child is not None:
            if force:
                restart = True
                self.deactivate(wait=True)
            else:
                return

        if method.lower() == "ip":
            self.method = "IP"
            if type(target) == str:
                target = [target]

            self.target = []
            for t in target:
                ip = ipaddress.ip_address(t)
                self.target.append(ip)

        elif method.lower() == "mac":
            self.method = "MAC"
            if type(target) == str:
                target = [target]

            self.target = []
            for t in target:
                if re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", t) is None:
                    raise ValueError("Incorrect MAC address passed in")
                else:
                    self.target.append(t.upper())
        else:
            raise ValueError("Incorrect method choice.")

        if restart:
            self.activate()

    def __ipCheck(self):
        attempt = 0
        while True:
            if self.__quit:
                return

            if self.testAll:
                triggered = True
            else:
                triggered = False

            for ip in self.target:
                if reachable(ip):
                    # Ping success
                    if not self.offline:
                        # Online Triggered
                        if self.testAll:
                            triggered = triggered and True
                        else:
                            triggered = triggered or True
                    else:
                        # Offline NOT Triggered
                        if self.testAll:
                            triggered = triggered and False
                else:
                    # Ping failed
                    if self.offline:
                        # Offline Triggered
                        if self.testAll:
                            triggered = triggered and True
                        else:
                            triggered = triggered or True
                    else:
                        # Online NOT Triggered
                        if self.testAll:
                            triggered = triggered and False
            if triggered:
                attempt += 1
                if attempt > self.retry:
                    self.callback(*self.args, **self.kwargs)
                    return
            else:
                attempt = 0

            if self.__quit:
                return
            time.sleep(self.interval)

    def __macCheck(self):
        print("MAC check")


def reachable(ip):
    try:
        socket.gethostbyaddr(ip.exploded)
        return True
    except socket.herror:
        response = os.system("ping -c 4 {0} > /dev/null 2>&1".format(ip.exploded))
        return response == 0


if __name__ == "__main__":
    print("HI")
