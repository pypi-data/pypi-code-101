"""
    Bws JsonRpc
    ~~~~~~~~~~~~~
    
    :author: Jose Delgado
    :email: esojangel@gmail.com
    Wrapper https://www.jsonrpcserver.com/
"""
__version__ = "0.0.2"

from typing import Any, Callable, Dict, Optional, cast
from flask import Blueprint, Response, request
from jsonrpcserver import  Result, Success, Error, dispatch
import inspect


Method = Callable[..., Result]
Methods = Dict[str, Method]

global_methods = dict()
global_class = dict()


def method(
    f: Optional[Method] = None, name: Optional[str] = None
) -> Callable[..., Any]:
    """
        @method(name='bar')
        def foo():
            pass
    """

    def decorator(func: Method) -> Method:
        nonlocal name
        global_methods[name or func.__name__] = func
        return func

    return decorator(f) if callable(f) else cast(Method, decorator)


class Group:
    """
        Group of methods
    """
    def __init__(self, name):
        self.name = name
    
    def method(
        self, f: Optional[Method] = None, name: Optional[str] = None
    ) -> Callable[..., Any]:
        """
            @method(name='bar')
            def foo():
                pass
        """

        def decorator(func: Method) -> Method:
            nonlocal name
            global_methods[self.name + '.' + name or func.__name__] = func
            return func

        return decorator(f) if callable(f) else cast(Method, decorator)

group = Group


def expose_class(k=None, name=None):
    """
        Expose One Class
    """
    def decorator(c):
        nonlocal name
        cname = name or c.__name__
        print(f"k: {k}, name: {name} cname: {cname}")
        for fname in dir(c):
            f = getattr(c, fname)
            if hasattr(f, '_urls_rpc') and f._urls_rpc:
                f_name = f._urls_rpc.pop()

                if not c in global_class:
                    global_class[c] = c()

                global_methods[cname + '.' + f_name] = getattr(global_class[c], fname)

        return c

    return decorator(k) if callable(k) else cast(Method, decorator)


def expose_method(f=None, name=None):
    """
        Use este decorador para responder json
    """
    def decorator(func):
        if not hasattr(func, '_urls_rpc'):
            func._urls_rpc = []
        func._urls_rpc.append(name or func.__name__)

        return f
    return decorator(f) if callable(f) else cast(Method, decorator)


class JSONRPCHandler:

    def as_blueprint(self, name=None):
        blueprint = Blueprint(name if name else "rpc", __name__)
        # blueprint.add_url_rule('', view_func=self.jsonrpc, methods=['POST'])
        blueprint.add_url_rule('/', view_func=self.jsonrpc, methods=['POST'])
        blueprint.add_url_rule('/docs', view_func=self.jsonrpc_docs, methods=['GET'])
        return blueprint

    def as_view(self):
        return self.jsonrpc

    def jsonrpc(self):
        payload = request.get_data().decode()
        # print(payload)

        results = dispatch(payload, methods=global_methods)
        return Response(
            results, 
            content_type="application/json"
        )


    def jsonrpc_docs(self):
        css = """
            <style>
                table { width: 100%;   border-collapse: collapse; }
                
                th, td { border: 1px solid black; }
            </style>
        """
        table = "<table >{}</table>"
        table_header = "<tr><th>Method</th><th>Doc</th></tr>"
        table_body = "".join([
            "<tr><td>{0}{1}</td><td>{2}</td></tr>".format(fname, self._get_args_str(f), self._get_doc_str(f))
            for fname, f in global_methods.items()
        ])
        result = css + table.format(table_header + table_body)
        return Response(result)
    
    def _get_args_str(self, func) -> str:
        
        return str(inspect.signature(func)).split("->")[0]
    
    def _get_doc_str(self, func) -> str:
        doc = func.__doc__ or ""
        return "<pre>{}</pre>".format("".join(doc.splitlines()))


rpc = JSONRPCHandler()

rpc.method = method
rpc.group = group
rpc.expose_class = expose_class
rpc.expose_method = expose_method
rpc.Success = Success
rpc.Error = Error