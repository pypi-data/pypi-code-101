"""
Git repo helper functions
"""
import functools
import os
import re
import tempfile
from collections import defaultdict
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.error import URLError

import git

from cocluremig.utils import github


def normalize_id_name(name: str) -> str:
    """
    Normalizes Names by removing special chars and whitespaces
    @param name: a string to clean
    @return: a cleaned string
    """
    name = re.sub(r"[^\w]", " ", name.casefold()).strip()  # Remove special Chars
    return "_".join(filter(lambda x: x, map(lambda x: x.strip().capitalize(),
                                            name.split(
                                                " "))))
    # Replace whitespace with Underscope and Capitalize Words


def get_remote_name(url: str) -> str:
    """
    Shortens remote identifiers
    @param url: the remotes url
    @return: an id
    """
    h = get_host(url)
    if "github" in h:
        user, project = github.parse_url(url)
        return normalize_id_name("GH___" + user + "__" + project)
    return normalize_id_name(url)


def get_repo(url: str, directory=None, remotes: Optional[List[str]] = None, add_all_remotes=False,
             no_fetch=False) -> git.Repo:
    """
    Clones or gets a git repo (bare)
    @param url: the repo's url
    @param directory: the repo save directory
    @param remotes: a list of remote urls
    @param add_all_remotes:
        if set to true tries to get & add all remotes
        via git-provider-api (only github implemented yet)
    @param no_fetch:
        if set to true does not fetch data from other machines
    @return:
        a git repo object
    """
    fldr_name = ".".join(url.split("/")[-2:])
    if directory is None:
        fldr_name = tempfile.gettempdir() + os.path.sep + fldr_name
    else:
        if not os.path.exists(directory):
            os.mkdir(directory)
        fldr_name = directory + os.path.sep + fldr_name
    if no_fetch:
        return git.Repo(fldr_name)
    if add_all_remotes:
        main_host = get_host(url)
        if main_host == "github.com":
            (user, project) = github.parse_url(url)
            if remotes is None:
                remotes = []
            try:
                (gh_remotes, _) = github.find_forks(user, project)
                remotes += gh_remotes
            except URLError:
                pass
    if os.path.exists(fldr_name):
        os.putenv("GIT_TERMINAL_PROMPT", "0")  # disable credential input prompts
        repo = git.Repo(fldr_name)
        if remotes is not None and not len(repo.remotes) == len(remotes) + 1:
            remote_names = list(map(lambda x: x.name, repo.remotes))
            for r in remotes:
                l_name = get_remote_name(r)
                if l_name not in remote_names:
                    nr = repo.create_remote(l_name, r)
                    with nr.config_writer as config_writer:
                        config_writer.set("fetch", "+refs/heads/*:refs/remotes/" + l_name + "/*")
    else:
        repo = git.Repo.clone_from(url, fldr_name, bare=True)
        if remotes is not None:
            for remote in remotes:
                repo.create_remote(get_remote_name(remote), remote)
        for remote in repo.remotes:
            with remote.config_writer as config_writer:
                config_writer.set("fetch", "+refs/heads/*:refs/remotes/" + remote.name + "/*")
        with repo.config_writer() as config_writer:
            config_writer.set_value("core", "askpass", "")
    try:
        for remote in repo.remotes:
            remote.fetch()
    except git.exc.GitCommandError as e:
        pass
    return repo


def get_host(url: str) -> str:
    """
    retrieves host-name from url
    @param url: a url
    @return: the host name
    """
    if url.startswith("http"):
        url = re.sub(r"http(s)?://", "", url)
        return url.split("/")[0]
    if url.startswith("ssh://"):
        url = url.lstrip("ssh://")
        return url.split(":")[0].split("@")[-1]
    if url.startswith("git://"):
        url = url.lstrip("git://")
        return url.split("/")[0]
    # assuming scp-style-ssh
    return url.split(":")[0].split("@")[-1]


def get_ref_names(repo: git.Repo,
                  ignore_tags: bool = False,
                  ignore_remotes: bool = False,
                  ignore_remotes_if_local_named: bool = True) \
        -> Dict[str, List[str]]:
    """
    Gets reference (branch, tag) names from repo

    @param repo: a git repository
    @param ignore_tags:
        if set to true does not consider tags
    @param ignore_remotes:
        if set to true does not consider names from remote repos
    @param ignore_remotes_if_local_named:
        if set to true does to consider names from remote repos
            if a name is alread present locally
    @return: a commit sha to refernce name(s) dictionary
    """
    refs: Dict[str, List[str]] = defaultdict(list)
    if not ignore_tags:
        for tag in repo.tags:
            refs[tag.commit.hexsha].append(tag.name)
    for local_ref in repo.heads:
        refs[local_ref.commit.hexsha].append(local_ref.name)
    if not ignore_remotes:
        for remote in repo.remotes:
            for remote_ref in remote.refs:
                if not refs.get(remote_ref.object.hexsha) or not ignore_remotes_if_local_named:
                    refs[remote_ref.object.hexsha].append(remote_ref.name)
    return refs


@functools.lru_cache(maxsize=2)
def get_edge_list(repo: git.Repo) -> Tuple[Iterable[Tuple[str, str]], Iterable[git.Commit]]:
    """
    Gets edge list of commit-graph
    @param repo:
    @return: A Tuple of
        - the edge list
        - the set of commits
    """
    edges: Iterable[Tuple[str, str]] = set()
    refs: Dict[str, List[str]] = get_ref_names(repo)
    processed_commits = set()
    for starting_point in refs.keys():
        for commit in repo.iter_commits(starting_point):
            sha = commit.hexsha
            for p in commit.parents:
                edges.add((sha, p.hexsha))
            processed_commits.add(commit)
    return (edges, processed_commits)
