import requests


class ZS_API:
    s: requests.Session = None
    hash: str = None
    debug: bool = False
    domain: str = "https://www.zippyshare.com"
    checked_files: list = []

    def check_account_created(self, username: str) -> bool:
        url = self.domain+"/rest/validate/validateUser"
        params = {
            "username": username
        }
        r = self.s.get(url, params=params)
        if self.debug:
            print("check_account_created", params, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot check account '{}' due to status code '{}'\n{}".format(username, r.status_code, r.content.decode()))
        return not r.json()


    def move_files(self, dir: int) -> bool:
        url = self.domain+"/rest/myAccount/moveToDir"
        ids = ";".join(str(_[0]) for _ in self.checked_files)
        data = {
            "ids": ids,
            "dirId": int(dir),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("move_files", data, r.status_code, r.content.decode())
        if r.status_code != 204:
            raise Exception("cannot move files '{}' to directory '{}' due to status code '{}'\n{}".format(
                ids,
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def set_directory_pw(self, dir: int, pw: str = None) -> bool:
        url = self.domain+"/rest/myAccount/passwordProtect"
        data = {
            "id": int(dir),
        }
        if pw:
            data.update({
                "passwordProtect": True,
                "password": pw,
            })
        else:
            data.update({
                "passwordProtect": False,
            })
        r = self.s.post(url, data=data)
        if self.debug:
            print("set_directory_pw", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot set directory '{}' password due to status code '{}'\n{}".format(
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def set_directory_access(self, dir: int, is_public: bool) -> bool:
        url = self.domain+"/rest/myAccount/makePublic"
        data = {
            "id": int(dir),
            "publicDir": is_public
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("set_directory_access", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot set directory '{}' access due to status code '{}'\n{}".format(
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def set_directory_view(self, dir: int, view: int) -> bool:
        url = self.domain+"/rest/myAccount/changeView"
        data = {
            "id": int(dir),
            "view": int(view),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("set_directory_view", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot set directory '{}' view to '{}' due to status code '{}'\n{}".format(
                dir,
                view,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def set_main_directory(self, dir: int) -> bool:
        url = self.domain+"/rest/myAccount/setAsMainDir"
        data = {
            "id": int(dir),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("set_main_directory", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot set directory '{}' as main directory due to status code '{}'\n{}".format(
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def rename_directory(self, name: str, dir: int) -> bool:
        url = self.domain+"/rest/myAccount/renameDir"
        data = {
            "newName": name,
            "dirId": int(dir),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("", data, r.status_code, r.content.decode())
        if r.status_code != 204:
            raise Exception("cannot rename directory '{}' to '{}' due to status code '{}'\n{}".format(
                dir,
                name,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def rename_file(self, name: str, file_id: int) -> bool:
        url = self.domain+"/rest/myAccount/renameFile"
        data = {
            "newName": name,
            "id": int(file_id),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("rename_file", data, r.status_code, r.content.decode())
        if r.status_code != 204:
            raise Exception("cannot rename file '{}' to '{}' due to status code '{}'\n{}".format(
                file_id,
                name,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def get_directory_stat(self, dir: int) -> dict:
        url = self.domain+"/rest/myAccount/deleteStats"
        data = {
            "ids": "d{}".format(dir),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("get_directory_stat", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot get directory stat '{}' due to status code '{}'\n{}".format(
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return r.json()

    def delete_files(self) -> bool:
        url = self.domain+"/rest/myAccount/delete"
        ids = ";".join(str(_[0]) for _ in self.checked_files)
        data = {
            "ids": ids,
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("delete_files", data, r.status_code, r.content.decode())
        if r.status_code != 204:
            raise Exception("cannot delete checked files '{}' due to status code '{}'\n{}".format(
                ids,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def delete_directory(self, dir: str) -> bool:
        url = self.domain+"/rest/myAccount/delete"
        data = {
            "ids": dir,
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("delete_directory", data, r.status_code, r.content.decode())
        if r.status_code != 204:
            raise Exception("cannot delete directory '{}' due to status code '{}'\n{}".format(
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True

    def create_directory(self, name: str, dir: int) -> bool:
        url = self.domain+"/rest/myAccount/createDir"
        data = {
            "name": name,
            "dirId": int(dir),
        }
        r = self.s.post(url, data=data)
        if self.debug:
            print("create_directory", data, r.status_code, r.content.decode())
        if r.status_code != 200:
            raise Exception("cannot create directory '{}' at directory '{}' due to status code '{}'\n{}".format(
                name,
                dir,
                r.status_code,
                r.content.decode(),
            ))
        return True


