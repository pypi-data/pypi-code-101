import re

import demjson
import execjs
import requests
from furl import furl


def resolve(embed_url, referer=None):
    response = requests.get(embed_url, headers={"Referer": referer or "http://103.194.171.18/"})
    decoded_text = execjs.eval(re.search(r"eval\((.*)\)", response.text).group(1))

    video_src_info: dict = demjson.decode(
        re.search(r"setup\((.*?)\);", decoded_text).group(1)
    )

    source_url_list = map(lambda x: x["file"], video_src_info["playlist"][0]["sources"])
    for url in source_url_list:
        if not furl(url).scheme:
            url = furl(scheme="https", host="fa.efek.stream").add(path=url).url

        return requests.get(url, headers={"Referer": embed_url}, stream=True)
