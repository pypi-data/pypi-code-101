try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

import json




def ErrorResponse(e): 
    error = eval(str(e))
    data = {'data':None,'state':False,'code': error[0], 'message': error[1]}
    res = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
    return res