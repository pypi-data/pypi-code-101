import requests
from my_utils.spidersystem.response import Response


class Downloader(object):

    def fetch(self, request):
        if request.method.upper() == "GET":
            resp = requests.get(request.url_with_query, headers=request.headers, proxies=request.proxies)
        elif request.method.upper() == "POST":
            resp = requests.post(request.url_with_query, headers=request.headers, body=request.body, proxies=request.proxies)
        else:
            raise Exception("Only support GET or POST MEthod!")
        return Response(request, status_code=resp.status_code, url=resp.url, headers=resp.headers, body=resp.content)


