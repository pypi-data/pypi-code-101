"""
纯python的功能函数
"""
import json
import pandas as pd


def f1():
    print('1')


def conv_queryset_ls_to_serialzer_ls(qs: list):
    """
    queryset数据的序列化
    """
    dcls = []
    if not qs:
        return dcls

    q = qs[0]
    kname_ls = list(q.keys())

    # 大于二维的数据序列化
    if kname_ls.__len__() > 2:
        for q in qs:
            dcls.append(q)
        return dcls
    else:
        kname, vname = kname_ls

    # 二维数据序列化
    for q in qs:
        k, v = q.get(kname), q.get(vname)
        dc = {
            kname: k,
            vname: v
        }
        dcls.append(dc)
    return dcls


def add_status_and_msg(dc_ls, status=200, msg=None):
    if status != 200 and msg is None:
        msg = '请求数据失败!'

    if status == 200 and msg is None:
        msg = "ok"

    ret = {
        'status': status,
        'msg': msg,
        'result': dc_ls
    }
    return ret


def show_json(data: dict):
    try:
        print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
    except:
        for k, v in data:
            print(k, ' --- ', v)


def add_space_prefix(text, n, more=True, prefix='\u3000'):
    text = str(text)
    if more:
        ret = prefix * n + text
    else:
        ret = prefix * (n - len(text)) + text
    return ret


def conv_df_to_serializer_data(df: pd.DataFrame, add_index=False) -> list:
    assert isinstance(df, pd.DataFrame), 'df的类型必须是DataFrame!'
    ret_ls = []
    for index, row in df.iterrows():
        k = row.index.tolist()
        v = row.values.tolist()
        data = dict(zip(k, v))

        if add_index:
            # 将df的index作为dc_ls的key
            data = {
                'name': index,
                'value': data
            }

        ret_ls.append(data)
    return ret_ls
