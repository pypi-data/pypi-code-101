"""用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取"""
from jmespath import search as jmes_search
from requests.models import Response
from json import loads as j_loads
from json import dumps as j_dumps


def extract(query=None, body=None):
    try:
        if type(body) is Response:
            body = body.json()
        if type(body) is str:
            body = j_loads(body)
        return jmes_search(query, body)
    except Exception as e:
        raise ValueError("Invalid query for `" + query + "`: " + str(e))


if __name__ == '__main__':
    from pyland.client import HTTPClient

    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100', method='GET').send()
    print(j_dumps(res.json(), indent=2, ensure_ascii=False))
    j_1 = extract(query='data.forecast[0].date', body=res.json())
    j_2 = extract(query='data.ganmao', body=res)
    print(j_1 + '\n' + j_2)
