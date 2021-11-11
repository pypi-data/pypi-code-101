from netdevsnmp.hostinfo.version import DeviceVersion
from netdevsnmp.vendors.alcatel.versions import AlcatelVersion
from netdevsnmp.vendors.arbor.versions import ArborVersion
from netdevsnmp.vendors.arista.versions import AristaVersion
from netdevsnmp.vendors.cisco.versions import CiscoVersion
from netdevsnmp.vendors.ericsson.versions import EricssonVersion
from netdevsnmp.vendors.extreme.versions import ExtremeVersion
from netdevsnmp.vendors.hpe.versions import HpeVersion
from netdevsnmp.vendors.huawei.versions import HuaweiVersion
from netdevsnmp.vendors.juniper.versions import JuniperVersion
from netdevsnmp.vendors.metamako.versions import MetamakoVersion
from netdevsnmp.vendors.synology.versions import SynologyVersion
from netdevsnmp.vendors.synology.oids import SynologyOids


def get_device_version(**kwargs):

    vendor = None
    for key in kwargs:
        if key == "vendor":
            vendor = kwargs[key]

    vendors = {}
    vendors["alcatel"] = AlcatelVersion
    vendors["arbor"] = ArborVersion
    vendors["arista"] = AristaVersion
    vendors["cisco"] = CiscoVersion
    vendors["ericsson"] = EricssonVersion
    vendors["extreme"] = ExtremeVersion
    vendors["hpe"] = HpeVersion
    vendors["huawei"] = HuaweiVersion
    vendors["juniper"] = JuniperVersion
    vendors["metamako"] = MetamakoVersion

    if vendor in vendors:
        return vendors[vendor](**kwargs)
    elif vendor == "net-snmp":
        if "snmp" in kwargs.keys():
            found_vendor = get_netsnmp_device_vendor(kwargs["snmp"])
            if found_vendor:
                if found_vendor == "synology":
                    kwargs["vendor"] = "synology"
                    return SynologyVersion(**kwargs)

    return DeviceVersion(**kwargs)


def get_netsnmp_device_vendor(snmp):

    s = SynologyOids()
    vartable = snmp.getnext(s.systemStatus)
    for varbind in vartable:
        for oid, value in varbind:
            if s.systemStatus in oid:
                return "synology"
    return None
