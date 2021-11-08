from .errors import *

import requests

SR = "https://some-random-api.ml"

class Image:
	def __init__(self , image_url: str):
		self.image_url_ = image_url

	@property
	def image_url(self):
		return self.image_url_

	def save(self):
		try:
			filename = self.image_url.split('/')[-1]
			r = requests.get(self.image_url , allow_redirects = True)
			open(filename , 'wb').write(r.content)
			return True
		except:
			return False
	

def image(endpoint: str):
	try:
		r = requests.request("GET", f"{SR}/img/{endpoint}").json()
		return r["link"]
	except:
		raise NotFound(f"Endpoint \"{endpoint}\" not found")

def dog():
	return image('dog')

def cat():
	return image('cat')

def fox():
	return image('fox')

def panda():
	return image('panda')

def red_panda():
	return image('red_panda')

def bird():
	return image('birb')

def koala():
	return image('koala')

def pikachu():
	return image('pikachu')

def kangaroo():
	return image('kangaroo')

def racoon():
	return image('racoon')

def whale():
	return image('whale')