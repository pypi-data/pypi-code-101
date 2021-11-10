import json, re

from asita.utils.router.route import Route
from asita.utils.sessions.session import Session
from asita.utils.sessions.sessions import Sessions

class Request():
    
    def __init__(self, data, route: Route, sessions: Sessions):
        """
            Permet de récupérer les informations d'une requête
            data: BaseHTTPRequestHandler, les informations de la requête
        """
        self.data = data
        self.sessions = sessions
        self.headers = data.headers
        self.route = route
        self.path: str = data.path
        self.request_type: str = data.command
        self.server_address: str = data.client_address
        self.server_version: str = data.server_version
        self.protocol_version: str = data.protocol_version

        self.params = self._parse_params()
        self.query = self._parse_query()
        self.body = self._parse_body()
        self.session = self._parse_session()

    def _parse_params(self):
        params = self.path.split('/')
        path_params = self.route.get_path().split('/')
        result = {}

        print(params, path_params)
        for i in range(len(path_params)):
            for j in range(len(params)):
                if i == j and re.match('^:(.*)$', params[j]):
                    result[params[j].replace(':', '')] = params[i]
        return result

    def _parse_session(self) -> Session:
        cookie = self.get('Cookie')
        if cookie:
            return self.sessions.get(cookie.split('=').pop())
        return Session(Sessions.random_session_id())

    def _parse_body(self):
        content_length = self.get('Content-Length')
        result = {}
        
        if content_length:
            body = self.data.rfile.read(int(content_length))
            if body:
                body = body.decode('utf8').replace("'", '"')
                result = json.loads(body)
        return result

    def _parse_query(self):
        chars = self.path.split('?')
        if len(chars) < 2:
            return {}
        chars = chars.pop().split('&')
        queries = {}
        for char in chars:
            char = char.split('=')
            queries[char[0]] = char[1]
        return queries

    def get(self, value) -> str:
        return self.headers.get(value)

    def accepts(self) -> str:
        return self.headers.get('accept')