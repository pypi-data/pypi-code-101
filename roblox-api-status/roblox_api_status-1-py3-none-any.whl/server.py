import flask
import requests
from .__init__ import api
responsecode = []
def status():
	global responsecode
	"""
	For get every roblox api's response code
	"""

	responsecode = []

	for x in range(199,299):
		responsecode.append(x+1)

	logs = []
	for key,val in api.items():
		code = requests.get(val).status_code
		result = "working" if code in responsecode else "not working"
		logs.append(f"{key} is {result} with response code {code}")
	with open("logs.txt","w") as fp:
		fp.write('\n'.join(logs))

app = flask.Flask('')
@app.route('/')
def index():
	return "<h1>Calling API... Please wait until API calling is done</h1>",302,{"Refresh":"0; result"}
@app.route('/result')
def res():
	status()
	with open("logs.txt") as fp:
		content = fp.read()
		content = content.replace("\n","<br>")
	return f"""
	<h1>List of API Status</h1>
	{content}<br><a href='down'>Here to go down api</a>
	"""
@app.route('/down')
def resdown():
	return "<h1>Calling API... Please wait until API calling is done</h1>",302,{"Refresh":"0; resdown"}
@app.route('/resdown')
def down():
	status()
	text = []
	with open("logs.txt") as fp:
		lines = fp.readlines()
		for line in lines:
			if "not working" in line:
				text.append(line)
	text = '<br>'.join(text)
	return f"""
	<h1>List of API that wasn't up</h1>
	{text}
	"""
@app.route('/<file>')
def access(file):
	try:
		return flask.send_file(file)
	except Exception:
		return "No file has asscoiated with the name"