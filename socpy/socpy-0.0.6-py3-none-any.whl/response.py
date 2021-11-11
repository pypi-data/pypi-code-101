from pandas import concat, json_normalize
from requests.models import Response

def coalesce_results(x):
    problems = concat([i['problems'] for i in x]).reset_index(drop = True)
    valid = concat([i['validated'] for i in x]).reset_index(drop = True)
    return {'problems': problems, 'valid': valid}

def soccer_enrich(resp, **kwargs):
    if not resp['problems']:
        valid = json_normalize(resp['validated'])
        if kwargs:
            for i in kwargs:
                valid[[i]] = kwargs[i]
        problems = json_normalize([{}])
    else:
        problems = json_normalize(resp['problems'])
        if kwargs:
            for i in kwargs:
                problems[[i]] = kwargs[i]
        valid = json_normalize([{}])
    return {"problems": problems, "validated": valid}

def soccer_resp(req):
    if not isinstance(req, Response):
        raise TypeError("'req' is not a request object")
    req_json = req.json()
    if "error" in req_json:
        problems = req_json
        valid = None
    else:
        problems = None
        valid = req_json
    return {"problems": problems, "validated": valid}