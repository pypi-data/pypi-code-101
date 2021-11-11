import os
import sys
from credsafe import Agent as credsafe
import pickle
from functools import partial
from omnitools import randstr, getpw
from easyrsa import EasyRSA
from aescipher import AESCipherCBC
import random
import string
import requests
from lxml import html


JSON_FP: str = "credsafe.zippyshare.json"


def create_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})
    s.post = partial(s.post, headers={
        "Accept": "application/json"
    })
    return s


def parse_credentials_argv():
    print("parsing credentials")
    credentials = []
    u = ["--username", "-U"]
    p = ["--password", "-P"]
    try:
        for i in range(0, len(sys.argv)):
            for k in u:
                if k == sys.argv[i]:
                    credentials.append(sys.argv[i+1])
                    break
        if len(credentials) == 0:
            print("skipped parse credentials")
            return credentials
        for i in range(0, len(sys.argv)):
            for k in p:
                if k == sys.argv[i]:
                    credentials.append(sys.argv[i+1])
                    break
        if len(credentials) == 2:
            print("parsed credentials")
            return credentials
        else:
            print("skipped parse credentials")
            return []
    except:
        print("skipped parse credentials")
        return []


def delete_credentials(json_fp=JSON_FP):
    if not os.path.isfile(json_fp):
        return
    if os.path.isfile(json_fp):
        print("deleting credentials")
        print("checking for file encryption")
        _ = _import_credentials(json_fp, True)
        os.remove(json_fp)
        if _:
            credsafe(app_name=_["app"], key_pair=_["kp"]).destroy(id=_["id"])
        print("deleted credentials")


def _import_credentials(json_fp=JSON_FP, alert: bool = False):
    _ = open(json_fp, "rb").read()
    try:
        _ = pickle.loads(_)
    except:
        if alert:
            print("decryption is required to delete credentials completely")
        what = "Enter master password to decrypt '{}'{{}}: ".format(json_fp)
        if alert:
            __ = getpw(what.format(" [ENTER to delete '{}' only]".format(json_fp)))
            print()
            if not __:
                return print("delete '{}' only".format(json_fp))
        else:
            __ = getpw(what.format(""))
            print()
        _ = AESCipherCBC(__).decrypt(_)
        _ = pickle.loads(_)
    return _


def import_credentials(json_fp=JSON_FP):
    if not os.path.isfile(json_fp):
        return
    print("importing credentials")
    _ = _import_credentials(json_fp)
    _ = credsafe(app_name=_["app"], key_pair=_["kp"]).get(id=_["id"], pw=_["pw"], k=_["k"])
    if not _:
        return print("skipped import credentials")
    print("imported credentials")
    return _


def export_credentials(credentials, json_fp=JSON_FP, overwrite: bool = False):
    if os.path.isfile(json_fp):
        if overwrite:
            delete_credentials(json_fp)
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
    credsafe(app_name=_["app"], key_pair=_["kp"]).set(id=_["id"], pw=_["pw"], k=_["k"], v=credentials)
    master_pw = getpw("Enter master password to encrypt '{}' [ENTER to skip encryption; CTRL+C to abort export]: ".format(json_fp))
    print()
    if master_pw is None:
        return print("aborted export: user initiated")
    _ = pickle.dumps(_)
    if not master_pw:
        open(json_fp, "wb").write(_)
    else:
        master_pw2 = getpw("Confirm master password to encrypt '{}' [CTRL+C to abort export]: ".format(json_fp))
        if master_pw2 is None:
            return print("aborted export: user initiated")
        if master_pw != master_pw2:
            return print("aborted export: mismatch master password")
        open(json_fp, "wb").write(AESCipherCBC(master_pw).encrypt(_).encode())
    print("exported credentials")


def gen_username(name):
    def upper_or_lower(_):
        if random.randint(0, 1) == 0:
            return _.lower()
        elif random.randint(0, 1) == 0:
            return _
        else:
            return _.upper()
    _ = name.split(" ")
    if random.randint(0, 1) == 0:
        username = upper_or_lower(_[1])
        username += "" if random.randint(0, 1) == 0 else "_"
        username += upper_or_lower(_[0])
        username += "" if random.randint(0, 1) == 0 else "_"
    else:
        username = upper_or_lower(_[0])
        username += "" if random.randint(0, 1) == 0 else "_"
        username += upper_or_lower(_[1])
        username += "" if random.randint(0, 1) == 0 else "_"
    bday = gen_birthday()
    random.shuffle(bday)
    if random.randint(0, 1) == 0:
        username += str(bday[0])
        username += "" if random.randint(0, 1) == 0 else "_"
    if random.randint(0, 1) == 0:
        username += str(bday[1])
        username += "" if random.randint(0, 1) == 0 else "_"
    if random.randint(0, 1) == 0:
        username += str(bday[2])
        username += "" if random.randint(0, 1) == 0 else "_"
    if username.endswith("_"):
        username = username[:-1]
    return username


def gen_password(length=20):
    return "".join(random.SystemRandom().choices(string.ascii_letters+string.digits, k=length))


def gen_birthday():
    return [
        random.SystemRandom().choice([i for i in range(1970, 1990+1)]),
        random.SystemRandom().choice([i for i in range(1, 12+1)]),
        random.SystemRandom().choice([i for i in range(1, 28+1)]),
    ]


def gen_email(username):
    _ = ["gmail.com","yahoo.com","hotmail.com","aol.com","hotmail.co.uk","hotmail.fr","msn.com","yahoo.fr","wanadoo.fr","orange.fr","comcast.net","yahoo.co.uk","yahoo.com.br","yahoo.co.in","live.com","rediffmail.com","free.fr","gmx.de","web.de","yandex.ru","ymail.com","libero.it","outlook.com","uol.com.br","bol.com.br","mail.ru","cox.net","hotmail.it","sbcglobal.net","sfr.fr","live.fr","verizon.net","live.co.uk","googlemail.com","yahoo.es","ig.com.br","live.nl","bigpond.com","terra.com.br","yahoo.it","neuf.fr","yahoo.de","alice.it","rocketmail.com","att.net","laposte.net","facebook.com","bellsouth.net","yahoo.in","hotmail.es","charter.net","yahoo.ca","yahoo.com.au","rambler.ru","hotmail.de","tiscali.it","shaw.ca","yahoo.co.jp","sky.com","earthlink.net","optonline.net","freenet.de","t-online.de","aliceadsl.fr","virgilio.it","home.nl","qq.com","telenet.be","me.com","yahoo.com.ar","tiscali.co.uk","yahoo.com.mx","voila.fr","gmx.net","mail.com","planet.nl","tin.it","live.it","ntlworld.com","arcor.de","yahoo.co.id","frontiernet.net","hetnet.nl","live.com.au","yahoo.com.sg","zonnet.nl","club-internet.fr","juno.com","optusnet.com.au","blueyonder.co.uk","bluewin.ch","skynet.be","sympatico.ca","windstream.net","mac.com","centurytel.net","chello.nl","live.ca","aim.com","bigpond.net.au"]
    return username+"@"+random.SystemRandom().choice(_)


def gen_name(names=[]):
    if not names:
        r = create_session().get("https://www.name-generator.org.uk/quick/")
        r = html.fromstring(r.content.decode())
        names.extend([_.replace("-", "") for _ in r.xpath("////form/h2[1]/following-sibling::div/text()")[:10]])
    return names


def generate_account_info():
    template = ""
    info = []
    for i in range(0, 10):
        _ = [
            *gen_name()[i].split(" "),
            gen_username(gen_name()[i]),
            gen_password(),
            gen_email(gen_username(gen_name()[i])),
        ]
        info.append(_)
        template += "{}\n{}\n{}\n{}\n{}\n\n".format(*_)
    open("zippy.txt", "wb").write(template.encode())
    return info


def read_account_info(s):
    credentials = [[]]
    for line in s.splitlines():
        if not line:
            credentials.append([])
            continue
        credentials[-1].append(line)
    return credentials


if __name__ == "__main__":
    generate_account_info()


