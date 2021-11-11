from netdevsnmp.hostinfo.version import DeviceVersion


class ArborVersion(DeviceVersion):
    def _get_version(self):
        for line in self._descriptions:
            if "Arbor Networks TMS" in line:
                self.os = "arbos"
                parts = line.split()
                if len(parts) > 3:
                    self.version = parts[3]

            if "Peakflow SP" in line:
                self.os = "arbos"
                parts = line.split()
                if len(parts) > 2:
                    self.version = parts[2]
