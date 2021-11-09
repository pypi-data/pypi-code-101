import re
from lxml import etree
import sys
sys.getsizeof()

class Response(object):

    def __init__(self, request, status_code, url, headers, body):
        """

        :param request:
        :param status_code:
        :param url: 如果有重定向则是重定向后的url
        :param headers:
        :param body:
        """
        self.request = request
        self.status_code = status_code
        self.url = url
        self.headers = headers
        self.body = body

    def xpath(self, rule):
        html = etree.HTML(self.body)
        return html.xpath(rule)

    def re_match(self, rule):
        return re.match(rule, self.body)

    def re_search(self, rule):
        return re.search(rule, self.body)

    def re_findall(self, rule):
        return re.findall(rule, self.body)