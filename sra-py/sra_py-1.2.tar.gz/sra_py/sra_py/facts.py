import requests

SR = "https://some-random-api.ml/facts/"

def fact(animal: str):
	r = requests.request("GET", SR+animal).json()
	return r['fact']