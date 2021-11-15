"""
Github-specific data-retrieval
"""
import json
import logging
import os
import re
import typing
from http.client import HTTPResponse
from typing import Pattern
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GITHUB_PREFIX: Pattern[str] = re.compile(r"^(((((git)|(ssh)|(http(s)?))://)?(git@)?github\.com(/|:)))")
GIT_POSTFIX: Pattern[str] = re.compile(r"\.git$")


def parse_url(url: str) -> typing.Tuple[str, str]:
    """
    retrieves project identifier from url
    @param url: a github url
    @return: user, project tuple
    """
    url = GITHUB_PREFIX.sub("", url.strip())
    url = GIT_POSTFIX.sub("", url)
    r_info = url.split("/")
    # user , project
    return (r_info[0], r_info[1])


def find_forks(user: str, project: str, params: typing.Dict = {'per_page': 100}, rec_forks: bool = True) \
        -> typing.Tuple[typing.List[str], typing.List[typing.Dict[str, typing.Any]]]:
    """
    Gets forks for github project
    @param user: project owner name
    @param project: project name
    @param params: github api-params
    @param rec_forks: if set to true also retrieves forks of forks
    @return: A tuple of
        - the fork urls
        - full github api-json for projects
    """
    json_out = []
    GITHUB_FORK_URL = "https://api.github.com/repos/{user}/{project}/forks"
    url = GITHUB_FORK_URL.format(user=user, project=project)
    if params:
        url = url + "?" + urlencode(params)
    header: __Header
    with _open_github_url(url) as result:
        result: HTTPResponse
        header = __parse_header(result)
        json_out += json.loads(result.read().decode(header['encoding']))
    while header.get("links"):
        if header.get("links").get("next"):
            with _open_github_url(header.get("links").get("next")) as next_page:
                header = __parse_header(next_page)
                json_out += json.loads(next_page.read().decode(header['encoding']))
        else:
            break
    if rec_forks:
        forked_forks = filter(lambda x: x['forks_count'], json_out)
        raw_ff = []
        for fork in forked_forks:
            _, raw = find_forks(fork['owner']['login'], fork['name'])
        json_out += raw_ff
    return (list(map(lambda x: x['clone_url'], filter(lambda x: not x['private'], json_out))), json_out)


def _open_github_url(url: str) -> HTTPResponse:
    logging.debug("opening %s", url)
    request = Request(url)
    if os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", "token " + os.environ.get("GITHUB_TOKEN"))
    else:
        logging.warning("No Github OAUTH-Token provided. Using public API.")
    return urlopen(request)


class __Header(typing.TypedDict):
    content: str
    encoding: str
    links: typing.Dict[str, str]


def __parse_header(response: HTTPResponse) -> __Header:
    headers = {'content':
                   response.getheader("content-type").split(";")[0],
               'encoding':
                   response.getheader("content-type").split(";")[-1].split("=")[-1].strip(),
               'links': {}}
    links = response.getheader("link")
    if links:
        for l in links.split(","):
            rel = ""
            url = ""
            for t in l.split(";"):
                if "rel=\"" in t:
                    rel = t.strip().lstrip("rel=").strip("\"")
                else:
                    url = t.strip().lstrip("<").rstrip(">")
            headers['links'][rel] = url
    return headers
