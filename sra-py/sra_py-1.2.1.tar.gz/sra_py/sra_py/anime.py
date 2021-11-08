import requests

SR = "https://some-random-api.ml"

class GIF:
	def __init__(self , gif_json):
		self.json = gif_json

	@property
	def gif_url(self):
		return self.json['link']

	def save(self):
		try:
			filename = self.gif_url.split('/')[-1]
			r = requests.get(self.gif_url , allow_redirects = True)
			open(filename , 'wb').write(r.content)
			return True
		except:
			return False

def wink():
	r = requests.request("GET", f"{SR}/wink").json()
	return GIF(r)

def pat():
	r = requests.request("GET", f"{SR}/pat").json()
	return GIF(r)

def hug():
	r = requests.request("GET", f"{SR}/hug").json()
	return GIF(r)