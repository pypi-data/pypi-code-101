try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    
import json


class Middleware():
    def __init__(self):
        pass
    

    def ErrorResponse(e): 
        error = eval(str(e))
        data = {'data':None,'state':False,'code': error[0], 'message': error[1]}
        res = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
        return res

    def Ok(e): 
        data = eval(str(e))
        data = {'data':data,'state':True,'code': None, 'message': None}
        res = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
        return res


if __name__ == '__main__':
   pass