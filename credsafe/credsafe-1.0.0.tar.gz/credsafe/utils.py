from omnitools import randstr, getpw
from aescipher import AESCipherCBC
from easyrsa import EasyRSA
from .agent import Agent
import pickle
import os


class Manager:
    def __init__(self, name: str):
        self.JSON_FP = "credsafe.{}.json".format(name)
    
    def delete_credentials(self):
        if not os.path.isfile(self.JSON_FP):
            return
        if os.path.isfile(self.JSON_FP):
            print("deleting credentials")
            print("checking for file encryption")
            _ = self._import_credentials(True)
            os.remove(self.JSON_FP)
            if _:
                Agent(app_name=_["app"], key_pair=_["kp"]).destroy(id=_["id"])
            print("deleted credentials")
    
    def _import_credentials(self, alert: bool = False):
        _ = open(self.JSON_FP, "rb").read()
        try:
            _ = pickle.loads(_)
        except:
            if alert:
                print("decryption is required to delete credentials completely")
            what = "Enter master password to decrypt '{}'{{}}: ".format(self.JSON_FP)
            if alert:
                __ = getpw(what.format(" [ENTER to delete '{}' only]".format(self.JSON_FP)))
                print()
                if not __:
                    return print("delete '{}' only".format(self.JSON_FP))
            else:
                __ = getpw(what.format(""))
                print()
            _ = AESCipherCBC(__).decrypt(_)
            _ = pickle.loads(_)
        return _
    
    def import_credentials(self):
        if not os.path.isfile(self.JSON_FP):
            return
        print("importing credentials")
        _ = self._import_credentials()
        _ = Agent(app_name=_["app"], key_pair=_["kp"]).get(id=_["id"], pw=_["pw"], k=_["k"])
        if not _:
            return print("skipped import credentials")
        print("imported credentials")
        return _
    
    def export_credentials(self, credentials, overwrite: bool = False):
        if os.path.isfile(self.JSON_FP):
            if overwrite:
                self.delete_credentials()
            else:
                return
        print("exporting credentials")
        _ = {
            "kp": EasyRSA(bits=1024).gen_key_pair(),
            "app": randstr(2**5),
            "id": randstr(2**5),
            "pw": randstr(2**5),
            "k": randstr(2**5),
        }
        Agent(app_name=_["app"], key_pair=_["kp"]).set(id=_["id"], pw=_["pw"], k=_["k"], v=credentials)
        master_pw = getpw("Enter master password to encrypt '{}' [ENTER to skip encryption; CTRL+C to abort export]: ".format(self.JSON_FP))
        print()
        if master_pw is None:
            return print("aborted export: user initiated")
        _ = pickle.dumps(_)
        if not master_pw:
            open(self.JSON_FP, "wb").write(_)
        else:
            master_pw2 = getpw("Confirm master password to encrypt '{}' [CTRL+C to abort export]: ".format(self.JSON_FP))
            if master_pw2 is None:
                return print("aborted export: user initiated")
            if master_pw != master_pw2:
                return print("aborted export: mismatch master password")
            open(self.JSON_FP, "wb").write(AESCipherCBC(master_pw).encrypt(_).encode())
        print("exported credentials")


