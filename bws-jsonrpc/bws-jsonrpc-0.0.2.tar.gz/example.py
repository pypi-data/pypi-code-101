"""
    Bws Collections
    ~~~~~~~~~~~~~
    
    :author: Jose Delgado
    :email: esojangel@gmail.com
    Wrapper https://www.jsonrpcserver.com/
"""

from flask import Flask
from bws_jsonrpc import (
    rpc,
    Result, 
    Success, 
    Error, 
    method, 
    group, 
    expose_class,
    expose_method,
    global_methods
)


@method
def ping() -> Result:
    '''return pong'''
    return Success("pong")


@method
def think(object, verb) -> Result:
    return Success([verb, object])


g = group("actions")
@g.method(name="drink")
def _drink_(object, verb="drink") -> Result:
    return Success([verb, object])


@expose_class(name="person")
class Person(object):
    
    @expose_method    
    def greet(self, name=None):
        '''
            return Hi + name
        '''
        return Success("Hi {}".format(name or ""))



if __name__ == "__main__":
    print(global_methods)
    app = Flask(__name__)
    # app.route("/", methods=["POST", "GET"])(http_dispatch)
    app.register_blueprint(rpc.as_blueprint())

    app.run(debug=True)