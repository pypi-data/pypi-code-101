import httpx


from .services import Auth, Firestore


def setup(config: dict):
    return Connection(config)


class Connection:

    def __init__(self, config: dict):
        self.api_key = config["apiKey"]
        self.project_id = config["projectID"]
        self.client = httpx.Client()

    def auth(self):
        return Auth(api_key=self.api_key, client=self.client)

    def firestore(self, idToken: str):
        return Firestore(api_key=self.api_key, project_id=self.project_id, client=self.client, id_token=idToken)
