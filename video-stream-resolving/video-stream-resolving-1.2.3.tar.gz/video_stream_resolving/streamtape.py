import re

import execjs
import requests
from lxml.etree import HTML


def _execute_code_generating_video_src_url(code):
    lines = code.strip().split(";")
    result = {}

    for l in lines:
        try:
            id_ = re.search(r"document\.getElementById\('(.+?)'\)", l).group(1)
        except:
            continue
        expr = l.split("=", 1)[1]
        url = execjs.eval(expr)

        result[id_] = url

    return result


def resolve(embed_url, referer=None) -> requests.models.Response:
    """
    :param embed_url: this param only accept url like https://streamtape.com/e/LqG4K9a8PKiRk1J
    :param referer:
    :return:
    """
    response = requests.get(embed_url, headers={"Referer": referer})
    if response.status_code == 500 or response.status_code == 404:
        return

    script_list = HTML(response.text).xpath("//script/text()")

    code_generating_video_src_url = list(filter(lambda s: "get_video" in s, script_list))[0]
    document_ready_code = list(filter(lambda s: "$(document).ready(function" in s, script_list))[0]

    id_ = re.search(r"\$\(['|\"]#(.+?)['|\"]\)\.", document_ready_code).group(1)
    result = _execute_code_generating_video_src_url(code_generating_video_src_url)

    src_url = f"https:{result[id_]}"
    response = requests.get(src_url, stream=True)

    return response