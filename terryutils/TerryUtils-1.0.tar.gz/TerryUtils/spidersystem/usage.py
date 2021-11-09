from my_utils.spidersystem.request import Request
from my_utils.spidersystem.downloader import Downloader

url = "https://www.baidu.com/s?wd=python"

q = Request(url="https://www.baidu.com", query={"wd":"python"})

print(q.url_with_query)

d = Downloader()


r = d.fetch(q)

print()




