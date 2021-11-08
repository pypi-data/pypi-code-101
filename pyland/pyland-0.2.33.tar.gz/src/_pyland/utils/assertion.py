"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""
from collections import Counter
from ..log import logger
from ..extractor import extract


def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error


def assert_search_api_pagination(func, param, ext_key="result.images[].id", ext_total="result.total"):
    """
    assert search apis with param offset and limit
    1. assert different offset should not has same response
    2. assert all pages num = total num
    api request example:
    {
        'offset': 0,
        'limit': 10
    }
    api response example:
    {
    'result':
        {
        'images': [
            {'id': 1},
            {'id': 2}
        ],
        'total': 2
        }
    }
    """
    response = func(param)
    total = extract(ext_total, response)
    pagination = 10 if total > 10 else 1

    num = 0
    res_all = []
    err_all = []
    for i in range(0, total, pagination):
        param.update({'limit': pagination, 'offset': i})
        res_id = extract(ext_key, func(param))
        logger.info(f'limit: {pagination}, offset: {i}, {ext_key} : {res_id}')
        res_all.extend(res_id)
        num += len(res_id)

    for r in Counter(res_all).items():
        logger.info(r)
        if r[1] > 1:
            err_all.append(r[0])
        else:
            continue
    logger.info(f"all results：{res_all}")
    if err_all:
        logger.error(f"duplicate results：{err_all}")
    assert total == num
    assert err_all == []
