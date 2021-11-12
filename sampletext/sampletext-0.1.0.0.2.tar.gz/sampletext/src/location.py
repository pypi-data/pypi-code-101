import requests
import json


def get_ip(ip):
    url = f"http://ipinfo.io/{ip}/json"
    request = requests.get(url)
    return request.json()
