import json
import random

import m3u8
import requests
from furl import furl


def resolve(embed_url, referer=None):
    video_id = furl(embed_url).args.get("data") or furl(embed_url).path.segments[-1]
    response = requests.post(
        f"https://jeniusplay.com/player/index.php?data={video_id}&do=getVideo",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36)",
            "x-requested-with": "XMLHttpRequest"},
        data={
            "hash": video_id,
            "r": referer or "https://195.2.81.61/"}
    )

    response = requests.get(json.loads(response.text)["videoSource"], headers={"Referer": "https://jeniusplay.com", "Accept": "*/*"})
    video_source_url_list = map(lambda x: x["uri"], m3u8.loads(response.text).data["playlists"])
    for url in video_source_url_list:
        response = requests.get(url, headers={"Referer": "https://jeniusplay.com/"})
        segments_url = random.choice(m3u8.loads(response.text).data["segments"])["uri"]

        response = requests.get(segments_url, stream=True)
        response.headers["content-type"] = "video/mp4"
        return response