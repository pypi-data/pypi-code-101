import os
import re

# import requests
import json

from . import VERSION

from pygitgrab.gitgrab import (
    set_trace,
    read_credits,
    getfolders,
    download_file,
    DEFAULT_CREDIT,
    DEFAULT_MAIN_CREDIT,
    expand_path,
    getrepo,
    getcontents,
    gettags,
    dump,
)
from pygitgrab.configreader import read_pull_config, read_pull_config_from_str
from pygitgrab.extract import extract
from pygitgrab.readuserinfo import get_credits


verbose_output = False


def print_t(*args, **kwargs):
    if verbose_output == True:
        print(*args, **kwargs)


def get_owner_repo(githuburl):

    regex = r"http[s]?:\/\/github\.com\/([^/]+)\/([^/]+)"

    matches = re.finditer(regex, githuburl)

    for matchNum, match in enumerate(matches, start=1):
        owner = match.group(1)
        repo = match.group(2)

        return owner, repo

    raise Exception(f"cant extract repo info, invalid github url='{githuburl}'")


def get_file_path(path, dest, pattern, root):
    if len(dest) == 0:
        if path.find(os.sep) >= 0:
            return path
        return root + os.sep + path
    pos = pattern.find("*")
    if pos >= 0:
        if not dest.endswith(os.sep):
            dest = dest + os.sep
        dest = dest + path[pos:]
    return dest


def check_valid_dir(basedir):

    curdir = os.getcwd()
    destdir = os.path.abspath(basedir)

    if not destdir.startswith(curdir):
        print(f"error: can not write to outbounded dir {destdir}")
        return False

    if len(destdir) == len(curdir):
        print(f"error: can not copy to base dir {destdir}")
        return False

    if len(basedir) == 0 or basedir == "." or basedir == os.sep:
        print(f"error: can not sync to base dir {destdir}")
        return False

    return True


def get_remote_pygg(login, githuburl):

    regex = r"http[s]?:\/\/github\.com\/([^/]+)\/([^/]+)\/([^?:]*)([?:]ref=(.+))?"

    try:
        match = re.search(regex, githuburl)

        print(match.groups())

        owner = match.group(1)
        repo = match.group(2)
        repo_path = match.group(3)
        repo_tag = match.group(5) if match.group(5) != None else "master"

        if match.group(5) == None:
            print_t("defaulting to master")

        baseurl = "https://api.github.com"
        repourl = f"{baseurl}/repos/{owner}/{repo}/contents/{repo_path}?ref={repo_tag}"

        print_t(repourl)

        content = download_file(repourl, auth=login)
        node = json.loads(content)
        download_url = node["download_url"]

        file_cont = download_file(download_url, auth=login).decode()

        return file_cont

    except Exception:
        raise Exception(f"cant extract repo info, invalid github url='{githuburl}'")


def gitgrab(login, simulate, config, cfgpath="pygg.cfg"):

    errors = 0

    for repo_alias, pulls in config.items():

        repo_url = pulls[0].repo
        repo_tag = pulls[0].tag

        owner, repo = get_owner_repo(repo_url)

        baseurl = "https://api.github.com"
        repourl = f"{baseurl}/repos/{owner}/{repo}/contents?ref={repo_tag}"

        print(f"pulling from {repourl}")

        allentries = getfolders(repourl, auth=login)
        allfiles = allentries.keys()

        for p in pulls:

            match = extract(p.pattern, allfiles)

            pulled = 0

            for m in match:

                pulled += 1
                entry = allentries[m]
                dest = get_file_path(entry.path, p.dest, p.pattern, repo_alias)
                url = entry.download_url

                basedir, fnam = os.path.split(dest)

                if not check_valid_dir(basedir):
                    errors += 1
                    continue

                print(f"copy {dest} - from url={url}")

                if simulate:
                    continue

                os.makedirs(basedir, exist_ok=True)

                if not download_file(url, dest, auth=login):
                    errors += 1

            if pulled == 0:
                print(f"nothing to pull for {p}")

    print(f"{cfgpath} done with {errors} errors")


def main_func():

    import argparse

    parser = argparse.ArgumentParser(
        prog="pygitgrab",
        usage="[python3 -m] %(prog)s [options]",
        description="grab files from remote git repo.",
        epilog="for more information refer to https://github.com/kr-g/pygitgrab",
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="show_version",
        action="store_true",
        help="show version info and exit",
        default=False,
    )
    parser.add_argument(
        "-V",
        "--verbose",
        dest="show_verbose",
        action="store_true",
        help="show more info",
        default=False,
    )
    parser.add_argument(
        "-L",
        "--license",
        dest="show_license",
        action="store_true",
        help="show license info and exit",
        default=False,
    )
    parser.add_argument(
        "-s",
        "--simulate",
        dest="simulate",
        action="store_true",
        help="dry run, do not download files",
        default=False,
    )

    sourcegroup = parser.add_mutually_exclusive_group()

    sourcegroup.add_argument(
        "-f",
        "--file",
        dest="files",
        action="append",
        type=str,
        nargs=1,
        help="name of pygg file to read, adds as '.pygg' extension if missing",
        default=None,
        metavar="FILE",
    )

    sourcegroup.add_argument(
        "-url",
        dest="urls",
        action="append",
        type=str,
        nargs=1,
        help="name of remote pygg file on github to read, adds as '.pygg' extension if missing",
        default=None,
        metavar="URL",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-u",
        "--user",
        dest="user",
        action="store",
        nargs="?",
        help="authenticate with user, no user for prompt. "
        + "create a personal access token in your github settings instead of using a password. "
        + "unauthenticated users have a lower rate for downloading from github. "
        + "https://developer.github.com/v3/rate_limit/ \n",
        default="",
    )

    group.add_argument(
        "-c",
        "--credits",
        dest="credits",
        action="store",
        nargs="?",
        help="read user and personal token from a file instead of prompting. "
        + f"make sure to put the file not in git controlled directory, (default: '{DEFAULT_CREDIT}')",
        default="",
    )

    group.add_argument(
        "-nc",
        "-ano",
        "--no-credits",
        "--anonymous",
        dest="nocredits",
        action="store_true",
        help=f"don't use the main credits file '{DEFAULT_MAIN_CREDIT}'",
        default=False,
    )

    inspectgroup = parser.add_mutually_exclusive_group()

    inspectgroup.add_argument(
        "-irepo",
        "--inspect-repo",
        dest="inspect_repo",
        action="store",
        nargs=1,
        help="read repo meta data",
        default=None,
    )

    inspectgroup.add_argument(
        "-idir",
        "--inspect-dir",
        dest="inspect_dir",
        action="store",
        nargs="+",
        help="read repo directory content",
        default=None,
    )

    inspectgroup.add_argument(
        "-itags",
        "--inspect-tags",
        dest="inspect_tags",
        action="store",
        nargs=1,
        help="read repo tags",
        default=None,
    )

    args = parser.parse_args()
    # print( args )

    if args.show_version:
        print("Version:", VERSION)
        return

    global verbose_output
    verbose_output = args.show_verbose
    if verbose_output:
        set_trace()

    if args.show_license:
        try:
            with open("LICENSE") as f:
                print(f.read())
        except:
            pass
        try:
            path = "LICENSE" + os.sep
            for sublicense in os.listdir(path):
                with open(path + sublicense) as f:
                    print("-" * 7, "incorporated license:", sublicense + "-" * 7)
                    print(f.read())
        except:
            pass
        return

    credits = args.credits
    if credits == None:
        credits = DEFAULT_CREDIT
    if credits != None and len(credits) == 0:
        if os.path.exists(expand_path(DEFAULT_MAIN_CREDIT)):
            credits = DEFAULT_MAIN_CREDIT
        else:
            credits = None
    if args.nocredits:
        credits = None

    login = None

    if credits != None:
        credits = read_credits(credits)

        try:
            user = credits[0]
            passwd = credits[1]
            login = (user, passwd)
        except:
            raise Exception("invalid credits file format")

    if login == None and (args.user == None or len(args.user) > 0):
        user, passwd = get_credits(args.user)
        login = (user, passwd)

    if login != None:
        print_t("downloading as user:", login[0])

    if args.inspect_repo:
        print_t("reading", args.inspect_repo)
        owner, repo = get_owner_repo(args.inspect_repo[0])
        print_t("reading", owner, repo)
        repo = getrepo(repo, login, owner=owner)
        dump(repo)
        return
    if args.inspect_dir:
        print_t("reading", args.inspect_dir)
        owner, repo = get_owner_repo(args.inspect_dir[0])  # todo branch ref
        print_t("reading", owner, repo)
        repo = getrepo(repo, login, owner=owner)
        path = args.inspect_dir[1] if len(args.inspect_dir) > 1 else None
        print_t("reading", path)
        cont = getcontents(repo, login, path)
        dump(cont)
        return
    if args.inspect_tags:
        print_t("reading", args.inspect_tags)
        owner, repo = get_owner_repo(args.inspect_tags[0])
        repo = getrepo(repo, login, owner=owner)
        cont = gettags(repo, login)
        dump(cont)
        return

    files = [["pygg.cfg"]] if args.files == None else args.files

    for f in files:
        fnam = f[0]
        if len(os.path.splitext(fnam)[1]) == 0:
            fnam += ".pygg"
        config = read_pull_config(fnam)
        gitgrab(login, args.simulate, config, cfgpath=fnam)

    urls = [] if args.urls == None else args.urls
    # print( urls )

    for url in urls:
        url = url[0]
        pygg = get_remote_pygg(login, url)
        config = read_pull_config_from_str(pygg)
        gitgrab(login, args.simulate, config, cfgpath=url)


def main():
    try:
        main_func()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        print("error:", ex)
