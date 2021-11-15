import copy
import string


def replace_data(data, pool):
    """
    替换数据
    :param data: 源数据，$name 或 ${name} 中的数据会被替换
    :param pool: 参数池，在参数池中匹配
    :return: 返回源数据替换后的数据，没匹配到不替换
    """
    if '$' not in str(data):
        return data

    # data为字典处理
    if isinstance(data, dict):
        copy_data = copy.deepcopy(data)
        for k, v in data.items():
            get_pool_data = None

            # key处理，$开头时处理，除去jsonPath表达式
            if k[0] == '$' and k[1] != '.' and k[1] != '{':
                # 从pool中取出变量替换
                get_pool_data = pool.get(k[1:])
            # ${}时处理
            elif k[0] == '$' and k[1] != '.' and k[1] == '{':
                get_pool_data = pool.get(k[2:-1])

            # 如果key中还有$，用string.Template来替换即可
            if '$' in k:
                get_pool_data = string.Template(k).safe_substitute(pool)

            if get_pool_data is not None:
                # 找到可替换的值时再赋值给key
                # 删除原来的key，新增现在的key和value
                del copy_data[k]
                k = get_pool_data

                copy_data[k] = v

            # value处理直接递归即可
            value = replace_data(v, pool)
            # 都用赋值方式操作，updata数据会为None
            copy_data[k] = value
        # 最终需要返回data,深拷贝是为了修改key
        data = copy_data


    # list和元组就循环递归处理
    elif isinstance(data, list):

        for i in range(len(data)):
            data[i] = replace_data(data[i], pool)
        return data

    # 元组处理
    elif isinstance(data, tuple):
        data_list = list(data)
        for i in range(len(data)):
            data_list[i] = replace_data(data[i], pool)
        data = tuple(data_list)
        return data

    # 字符串处理，除去上面的，如果包含$的都是字符串处理,但是为了匹配数据类型，还是得判断一下
    else:
        # 从数据池获取替换
        if data[0] == '$' and data[1] != '.' and data[1] != '{':
            slices_data = data[1:]
        elif data[0] == '$' and data[1] != '.' and data[1] == '{':
            slices_data = data[2:-1]
        else:
            # 如果其中还有$，就直接字符串模版方式替换
            return string.Template(str(data)).safe_substitute(pool)

        res = pool.get(slices_data)

        if res is not None:
            return res
        # 如果没获取到就返回本身
        else:
            return data

    return data


if __name__ == '__main__':
    pool = {'name': '张三', 'age': 13,'gender':[1,23]}
    data = {'${name}，李四': '${age}', 'test': [{'$age': '$age'}, ('$name', '$age'), ({'$age': '$name'})], 'testdic': {'name': {'$name': '$age'}},'gender':"$gender",'aaa':"$bbb"}
    res = replace_data(data, pool)
    print(res)
