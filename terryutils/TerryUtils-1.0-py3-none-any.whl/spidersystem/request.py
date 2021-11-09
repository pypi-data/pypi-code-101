# 构建一个请求对象
import urllib.parse

class Request(object):

    def __init__(self, url, method="GET", query={}, body={}, proxies={}, spider_name="request", headers=None):
        self.url = url
        self.method = method

        if not isinstance(query, dict):
            raise Exception("query must be a dict")
        self.query = query

        if not isinstance(body, dict):
            raise Exception("body must be a dict")

        self.body = body
        self.proxies = proxies
        self.headers = headers
        self.spider_name = spider_name

    @property
    def url_with_query(self):
        '''将请求参数字典和url地址拼接'''
        url = self.url
        _ = urllib.parse.urlparse(url)
        url_without_query = _.scheme + "://" + _.hostname + _.path
        url_query = urllib.parse.parse_qsl(_.query)

        query = self.query.items()
        all_query = sorted(set(list(query) + url_query))

        return url_without_query + "?" + urllib.parse.urlencode(all_query)