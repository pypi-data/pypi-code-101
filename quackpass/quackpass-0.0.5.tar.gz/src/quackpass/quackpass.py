
# ----- > Simple Secure Password Program
import hashlib
import os
import json

class SimpleLogin():
	def __init__(self, salt="", file="passwords.txt"):
		self.salt = salt
		self.file = file
		if not os.path.isfile(self.file):
			os.system(f'touch {self.file}')
			with open(self.file, 'w') as file:
				file.write(json.dumps({'full_data':[], 'usernames':[]}))

	def check(self, username, password):
		passphrase = hashlib.sha256(f"{password}{self.salt}".encode()).hexdigest()
		userphrase = hashlib.sha256(f"{username}{self.salt}".encode()).hexdigest()
		total = passphrase+userphrase
		with open(self.file, 'r') as file:
			data = json.loads(file.read())
		if total in data['full_data']:
			return True
		else:
			return False

	def login(self, username_prompt="Username: ", password_prompt="Password: "):
		logged_in = False
		username = ""
		while not logged_in:
			username = input(username_prompt)
			password = input(password_prompt)
			if self.check(username, password):
				return username
			else:
				print("Incorrect Password or Username")
		return username

	def add_user(self, username, password, overwrite=False):
		with open(self.file, 'r') as file:
			data = json.loads(file.read())
			passphrase = hashlib.sha256(f"{password}{self.salt}".encode()).hexdigest()
			userphrase = hashlib.sha256(f"{username}{self.salt}".encode()).hexdigest()
			total = passphrase+userphrase
			if userphrase not in data['usernames']:
				data['usernames'].append(userphrase)
				data['full_data'].append(total)
				with open(self.file, 'w') as file:
					file.write(json.dumps(data))
			else:
				if overwrite:
					data['usernames'].append(userphrase)
					data['full_data'].append(total)
					with open(self.file, 'w') as file:
						file.write(json.dumps(data))
				else:
					return False

