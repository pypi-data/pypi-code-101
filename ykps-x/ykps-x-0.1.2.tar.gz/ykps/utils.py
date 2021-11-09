import requests


class Page:

    def __init__(self, url: str):
        self.session = requests.Session()
        self.response = self.session.get(url, allow_redirects=True)

    @property
    def text(self):
        return self.response.text
