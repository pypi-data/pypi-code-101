from werkzeug.wrappers import Request, Response, ResponseStream

class Data(object):
    def __init__(self, **kwargs):
        self.data = kwargs.get('data', None)
        self.message = kwargs.get('message', None)
        self.code = kwargs.get('code', None)
        self.state = kwargs.get('state', None)


class DataResponseMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.app(request)
        if isinstance(response, Response):
            return response(environ, start_response)
        elif isinstance(response, ResponseStream):
            return response(environ, start_response)
        else:
            raise Exception('response must be Response or ResponseStream')



class FrameResponseMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response()
        response.status_code = 200
        response.mimetype = 'application/json'
        response.data = self.app(request, response)
        return response(environ, start_response)



class LoginResponseMiddleware(object):
    '''
    Simple Response middleware
    '''

    def __init__(self, app, username, password):
        self.app = app
        self.userName = username
        self.password = password

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']
        
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if userName == self.userName and password == self.password:
            environ['user'] = { 'name': self.userName }
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'application/json', status=401)
        return res(environ, start_response)