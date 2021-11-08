import requests

SR = "https://some-random-api.ml"

class Pokemon:
	def __init__(self , pokemon_json):
		self.json = pokemon_json
		self.stats = self.json['stats']
		self.family = self.json['family']

	@property
	def name(self):
		return self.json['name']

	@property
	def id_(self):
		return self.json['id']

	@property
	def type(self):
		return self.json['type']
	
	@property
	def species(self):
		return self.json['species']

	@property
	def image_url(self):
		return self.json['sprites']['normal']

	@property
	def gif_url(self):
		return self.json['sprites']['animated']
	
	@property
	def weight(self):
		return self.json['weight']

	@property
	def height(self):
		return self.json['height']

	@property
	def gender(self):
		return self.json['gender']

	@property
	def description(self):
		return self.json['description']

	@property
	def generation(self):
		return self.json['generation']

	@property
	def abilities(self):
		return self.json['abilities']

	@property
	def base_experience(self):
		return self.json['base_experience']

	@property
	def hp(self):
		return self.stats['hp']

	@property
	def attack(self):
		return self.stats['attack']
	
	@property
	def defence(self):
		return self.stats['defence']

	@property
	def speed(self):
		return self.stats['speed']

	@property
	def sp_attack(self):
		return self.stats['sp_atk']
	
	@property
	def sp_defence(self):
		return self.stats['sp_def']

	@property
	def total(self):
		return self.stats['total']

	@property
	def egg_groups(self):
		return self.json['egg_groups']

	@property
	def evolution_stage(self):
		return self.family['evolutionStage']

	@property
	def evolution_line(self):
		return self.family['evolutionLine']

def pokedex(pokemon):
	r = requests.request("GET", f"{SR}/pokedex?pokemon={pokemon}").json()
	print(r)
	return Pokemon(r)