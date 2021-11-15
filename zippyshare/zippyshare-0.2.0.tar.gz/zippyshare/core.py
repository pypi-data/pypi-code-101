from omnitools import getpw, parse_credentials_argv
from .filemanager import ZS_FM, sha3_512hd
from .utils import csm, create_session
from lxml import html
import vpncmd
import time
import re


class ZS(ZS_FM):
    def __init__(self, *, vpncmd_option = None, vpncmd_setup_cmd_option = None, **kwargs):
        super().__init__(**kwargs)
        if vpncmd_option and vpncmd_setup_cmd_option:
            self.vpncmd = vpncmd.VPNCMD(**(vpncmd_option or {}))
            self.vpncmd.setup_cmd(*(vpncmd_setup_cmd_option or []))

    def connect_vpn(self, _NICNAME):
        if self.debug:
            print("connecting to vpn")
        self.vpncmd.connect_known_vpn(_NICNAME)
        while not self.vpncmd.is_connected_to_vpn():
            time.sleep(0.5)
        if self.debug:
            print("connected to vpn")

    def disconnect_vpn(self):
        if self.debug:
            print("disconnecting vpn")
        self.vpncmd.disconnect_vpn()
        if self.debug:
            print("disconnected vpn")

    def login(self, credentials = None, use_vpn: bool = True, _NICNAME: str = "VPN2"):
        self.s = create_session()
        if use_vpn:
            self.connect_vpn(_NICNAME)
        if not credentials:
            credentials = parse_credentials_argv(True)
            if credentials:
                csm.export_credentials(credentials, overwrite=True)
            else:
                credentials = csm.import_credentials()
                if not credentials:
                    credentials = [
                        input("Enter username: "),
                        getpw("Enter password: "),
                    ]
                    print()
                    csm.export_credentials(credentials)
        if self.debug:
            print("logging in")
        self.s.get(self.domain)
        self.s.post(self.domain+"/services/login", data={
            "login": credentials[0],
            "pass": credentials[1],
            "remember": "on",
        })
        r = self.s.get(self.domain)
        r = html.fromstring(r.content.decode())
        try:
            username = r.xpath("//*[@class='login']/span[1]/text()")[0][7:]
            if credentials[0] != str(username):
                raise
            self.hash = sha3_512hd(sha3_512hd(sha3_512hd(credentials[1])))
        except:
            raise Exception("cannot login, please check your credentials")
        if self.debug:
            print("logged in")

    def __del__(self):
        self.logout()

    def logout(self):
        if self.debug:
            print("logging out")
        self.s.get(self.domain+"/services/logout")
        self.s.close()
        self.s = None
        if self.debug:
            print("logged out")
        self.disconnect_vpn()

    def upload(self):
        raise NotImplementedError

    def remote_upload(self, remote_url, private: bool = True):
        if self.debug:
            print("remote uploading '{}'".format(remote_url))
        r = self.s.get(self.domain)
        r = html.fromstring(r.content.decode())
        action = r.xpath("//form[@name='upload_form2']/@action")[0]
        if action.startswith("//"):
            action = "https:"+action
        data = {"file1": remote_url}
        if private:
            data.update({"private": "checkbox"})
        r = self.s.post(action, data=data)
        if r.status_code != 200:
            raise Exception("cannot upload remote_url '{}' [{}] ({})".format(remote_url, r.status_code, r.content.decode()))
        r = html.fromstring(r.content.decode())
        text_field = r.xpath("//input[@class='text_field']/@value")[0]
        if self.debug:
            print("remote uploaded '{}'".format(remote_url))
        return text_field

    @staticmethod
    def get_link(file_url, refresh_ttd: bool = False, _s = None):
        s = _s or create_session()
        r = s.get(file_url)
        domain = "/".join(file_url.split("/")[:3])
        id = file_url.split("/")[-2]
        link = re.search(r".(/d/{}/)..*?\((.*?)\).*?(.)(/.*?)\3.*$".format(id), r.content.decode(), flags=re.MULTILINE)
        if not link:
            raise Exception("file not found '{}' [{}]".format(id, r.status_code))
        link = domain + link[1] + str(eval(link[2])) + link[4]
        if refresh_ttd:
            return lambda : (_s or s).get(link, headers={"Range": "bytes=0-1"})
        return link

    @staticmethod
    def refresh_ttd(file_url):
        return ZS.get_link(file_url, refresh_ttd=True)()

