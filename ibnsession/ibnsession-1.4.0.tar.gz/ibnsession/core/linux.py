# -*- coding: UTF-8 -*-

from netmiko import ConnectHandler
from collections import namedtuple

class base_linux(object):
    def __init__(self,ac_info,dev_info):
        self.username = ac_info.username
        self.password = ac_info.password

    def account_verification(self):
        return False





# -----------------------------------------------------------------------------
class centos(base_linux):
    def gen_routing_policy(self):
        return []


class ubuntu(base_linux):
    def gen_routing_policy(self):
        return []

class debian(base_linux):
    def gen_routing_policy(self):
        return []

class suse(base_linux):
    def gen_routing_policy(self):
        return []