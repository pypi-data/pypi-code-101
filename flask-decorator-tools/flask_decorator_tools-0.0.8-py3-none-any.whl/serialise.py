import functools
from flask import make_response, request
import json


def serialize_obj(obj):
    '''Used to convert a class to json'''
    return obj.__dict__

def toJSONResponse(object):
    '''Convert an object to json response'''
    data = object.__dict__
    response = make_response(json.dumps(data, default = serialize_obj))
    response.headers['Content-Type'] = 'application/json'
    ##print(json.dumps(data, default = serialize))
    return response

def deserialise(klass):
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            body = request.json
            deserialise_body = klass(body)
            return funct(deserialise_body, *args, **kwargs)
        return wrapper
    return decorator

def deserialise_args(klass):
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            body = request.args
            deserialise_body = klass(body)
            return funct(deserialise_body, *args, **kwargs)
        return wrapper
    return decorator

def serialise():
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            output = funct(*args, **kwargs)
            data = output
            code = 0
            # check if a repsonse code is also returned
            if isinstance(output, tuple):
                data = output[0]
                code = output[1]
            else:
                code = 200
            if isinstance(data, str):
                return data, code
            return toJSONResponse(data), code
        return wrapper
    return decorator