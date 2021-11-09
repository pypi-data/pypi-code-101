import requests
from lxml.etree import HTML


def resolve(web_url, referer=None):
    response = requests.get(web_url)
    video_src_url = list(filter(lambda e: "?tokenkey" in e, HTML(response.text).xpath("//source/@src")))[0]
    return requests.get(video_src_url, headers={"Referer": web_url}, stream=True)