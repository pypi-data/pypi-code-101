import http
import json
from typing import Union

import requests
from cbaxter1988_models.src.http_response_models import ProblemDetailModel, PROBLEM_DETAIL_HEADER_JSON


def get_html_page(url) -> str:
    return requests.get(url).text


def get_request(url):
    return requests.get(url)


def post_request(url, body):
    response = requests.post(url=url, json=body, headers={"Content-Type": "application/json"})
    return response


