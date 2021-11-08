import sys
import os
import json
import requests
import textwrap

baseurl = "https://api.github.com"
DEFAULT_CREDIT = "~/pygg.credits.txt"
DEFAULT_MAIN_CREDIT = "~/.pygg_credits"


DEBUG = False


def set_trace():
    global DEBUG
    DEBUG = True


def print_t(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def dump_t(o):
    if DEBUG:
        dump(o)


def dump(o):
    if type(o) == str:
        for line in o.splitlines():
            print(
                line,
            )
    else:
        try:
            for line in json.dumps(o, indent=4, sort_keys=True).splitlines():
                print(
                    line,
                )
        except:
            o = textwrap.wrap(str(o))
            for line in o:
                print(
                    line,
                )


def expand_path(fnam):
    fnam = os.path.expanduser(fnam)
    fnam = os.path.expandvars(fnam)
    fnam = os.path.abspath(fnam)
    return fnam


def read_credits(credits_file=None):
    if credits_file == None:
        credits_file = DEFAULT_CREDIT
    credits_file = expand_path(credits_file)
    credits = None
    with open(credits_file) as f:
        content = f.read().splitlines()
        content = map(lambda x: x.strip(), content)
        content = list(filter(lambda x: len(x) > 0, content))
        credits = content[0], content[1]
    return credits


class Entry:
    def __init__(self, args):
        self.__dict__.update(args)

    def __repr__(self):
        return f"Entry< path='{self.path}' type='{self.type}' size={self.size} url='{self.download_url}' >"


def _getheaders(auth):
    headers = {"User-Agent": "pygg" if auth is None else auth[0]}
    return headers


def getfolder(url, auth=None):

    headers = _getheaders(auth)
    with requests.get(url, auth=auth, headers=headers) as r:

        if r.status_code != 200:
            raise Exception("can not load data", url, r.headers)

        raw = r.content
        body = raw.decode()
        data = json.loads(body)

        all = {}

        for entry in data:
            if isinstance(entry, str):
                raise Exception(data, r.headers)

            e = Entry(entry)
            all[e.path] = e

        return all


def getfolders(repourl, auth=None):

    all = {}
    entries = getfolder(repourl, auth=auth)

    for path, entry in entries.items():

        if entry.type == "dir":
            sub = getfolders(entry.url, auth=auth)
            all.update(sub)
        else:
            all[path] = entry

    return all


def download_file(url, dest=None, auth=None):
    try:
        headers = _getheaders(auth)

        with requests.get(url, auth=auth, headers=headers) as r:

            if r.status_code != 200:
                print_t(r.url)
                dump_t(r)
                raise Exception("can not load data", url, r.status_code, r.headers)

            data = r.content

            if dest != None:
                with open(dest, "wb") as f:
                    f.write(data)

                    return True
            else:
                return data

    except Exception as ex:
        print("error: ", dump_t(ex))

    return False if dest != None else None


def download_json(url, dest=None, auth=None):
    content = download_file(url, auth=auth)
    if content:
        o = json.loads(content)
        if dest != None:
            with open(dest, "w") as f:
                f.write(json.dumps(o, indent=4))
        return o


def getallpages(url, auth):

    page = 1
    elems = []

    while True:

        try:

            repourl = f"{url}?page={page}"

            print("download page", page)
            o = download_json(repourl, auth=login)

            if len(o) == 0:
                break

            elems.extend(o)

            page += 1

        except Exception as ex:
            print("error: ", ex)
            raise

    return elems


def sort_name(olist, skey=None):
    if skey == None:
        skey = "name"
    olist.sort(key=lambda x: x[skey].lower())


def getrepos(auth, dest=None):

    repourl = f"{baseurl}/user/repos"

    repos = getallpages(repourl, auth)

    if dest != None:
        with open(dest, "w") as f:
            f.write(json.dumps(repos, indent=4))

    print_t("repos", len(repos))

    return repos


def getrepo(repo, auth, owner=None, dest=None):

    if owner == None:
        owner = auth[0]

    repourl = f"{baseurl}/repos/{owner}/{repo}"
    print_t("repourl", repourl)

    o = download_json(repourl, auth=auth, dest=dest)

    return o


def getelem(repo, elem, auth, owner=None, dest=None):

    nav = repo

    for nam in elem.split("."):
        nav = nav[nam]

    url = nav

    o = download_json(url, auth=auth, dest=dest)


def getcontents(repo, auth, path=None, dest=None, sorted=False):

    name = repo["name"]
    owner = repo["owner"]["login"]

    if path == None:
        path = ""

    repourl = f"https://api.github.com/repos/{owner}/{name}/contents/{path}"
    o = download_json(repourl, auth=auth, dest=dest)

    if sorted:
        sort_name(o)

    return o


def gettags(repo, auth, dest=None):

    name = repo["name"]
    owner = repo["owner"]["login"]

    repourl = f"https://api.github.com/repos/{owner}/{name}/git/refs/tags"
    o = download_json(repourl, auth=auth, dest=dest)
    return o


if __name__ == "__main__":

    set_trace()

    login = read_credits()

    # repos = getrepos(login)
    # dump_t( repos )

    repo = getrepo("pygitgrab", login)
    dump_t(repo)

    tags = gettags(repo, login)
    dump_t(tags)

    tags = getcontents(repo, login)
    dump_t(tags)
