def merge_dict(dic1, dic2):
    """
    合并两个字典,有相同的就更新，不相同的就添加
    :param dic1: 基本数据
    :param dic2: 以dic2数据为准，dic1和dic2都有的数据，合并后以dic2为准
    :return: 合并后的字典
    """

    #解决value递归时不是字典情况
    if isinstance(dic2,dict):
        dic1 = dic2
        return dic1

    for k, v in dic2.items():
        dic1Value = dic1.get(k)

        if isinstance(v, dict):
            if not isinstance(dic1Value, dict):
                # 如果dic1中没有dic2的key的数据，或dic1value的数据类型是list(就是两者数据类型不同时，直接赋值),直接赋值dic2的value给dic1
                dic1[k] = v
            else:
                merge_dict(dic1[k], dic2[k])
        # 如果是list再继续循环去遍历
        elif isinstance(v, list) or isinstance(v, tuple):

            for i in range(len(v)):
                # 不是元组或list时，直接赋值
                if not isinstance(dic1Value, (list, tuple)):
                    # 如果dic1中没有dic2的key的数据，或dic1value的数据类型是dict(就是两者数据类型不同时，直接赋值),直接赋值dic2的value给dic1
                    dic1[k] = v
                # 表示dic2和dic1的value都是列表时处理
                else:
                    try:
                        merge_dict(dic1[k][i], v[i])
                    except IndexError:
                        # 抛异常说明dic1的list中没有这么多数据，就直接append添加dic2中的数据过来即可。
                        dic1[k].append(v[i])

        # 如果不是字典也不是list,就直接把dic2的值替换给dic1，以dic2的值为准
        else:
            dic1[k] = v
    return dic1


if __name__ == '__main__':
    # 示例：
    d1 = {
        'name': 'xs',
        'age': 18,
        'data': [{'api3': 'api3'}, {'api4': 'api4'}],
        'testlist': {'method': 'post', 'testlist': [{'list3': 'li3', 'list9': 'list9'}, {'list4': 'list4'}]},
        'testlist2': {'method': 'post', 'testlist': {'list5': 'li5'}},
        'testlist3': {'tup': ({'name': 'aa'},123), 'testlist': [{'list5': 'li5'},123, {'list6': 'list6'}]},
        'testlist4': {'tup': ({'name': 'aa'},[{'age':'123'},(123,145),'abcd'])}

    }

    d2 = {
        'age': 19,
        'path': 'xxx/path',
        'method': {'method': 'get'},
        'testlist': {'method': 'get', 'testlist': [{'list3': 'li1'}, {'list7': 'list7'}, {'list8': 'list8'}]},
        'testlist2': {'method': 'get', 'testlist': [{'list6': 'li6'}]},
        'data': [{'api': 'api1'}, {'api4': 'api2'}, {'api5': 'api5'}],
        'testlist3': {'tup': ({'name': 'bb'},333), 'testlist': [{'list5': 'li5'},234, {'list7': 'list7'}]},
        'testlist4': {'tup': ({'name': 'bb'},[{'age':'456','name':'xx'},(456,789),'dddd'])}
    }

    print(merge_dict(d1, d2))
