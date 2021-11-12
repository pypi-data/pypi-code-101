import requests
from cinemat.config import OMDB_URL, OMDBAPI_KEY


url = f"{OMDB_URL}/?apikey={OMDBAPI_KEY}&"


def make_get(parameters):
    response = requests.get(url, params=parameters).json()
    return response
