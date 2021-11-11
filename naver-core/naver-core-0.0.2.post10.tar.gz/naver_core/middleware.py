import json


def jsonConvert(data):
    return json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))


def ErrorResponse(e):
    if isinstance(e, ValueError):
        return {'data': None, 'state': False, 'code': 400, 'message': e.args[0]}
    if isinstance(e, TypeError):
        return {'data': None, 'state': False, 'code': 500, 'message': e.args[0]}
    if isinstance(e, dict):
        return e
    print(str(e))
    error = eval(str(e))
    data = {'data': None, 'state': False,
            'code': error[0], 'message': error[1]}
    res = jsonConvert(data)
    return res


def Ok(e):
    if isinstance(e, dict):
        return {'data': e, 'state': True, 'code': None, 'message': None}
    if isinstance(e, list):
        l = []
        for i in e:
            l.append(json.loads(i))
        return {'data': l, 'state': True, 'code': None, 'message': None}
    data = e
    data = {'data': data, 'state': True, 'code': None, 'message': None}
    res = jsonConvert(data)
    return res


def getValue(input, key):
    data = input.get('data')
    if isinstance(data, dict):
        if key in data:
            return data[key]
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    pass
