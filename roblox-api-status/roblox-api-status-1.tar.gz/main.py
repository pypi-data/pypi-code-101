import flask
import requests
responsecode = []
def status():
	global responsecode
	"""
	For get every roblox api's response code
	"""

	print('Begin Test all roblox API and check status')

	api = {
		"Account Information":"https://accountinformation.roblox.com/",
		"Account Settings":"https://accountsettings.roblox.com/",
		"Advertising Configuration":"https://adconfiguration.roblox.com/",
		"Advertisement":"https://ads.roblox.com/",
		"Assets Delivery":"https://assetdelivery.roblox.com/",
		"Authenication":"https://auth.roblox.com/",
		"Avatar":"https://avatar.roblox.com/",
		"Badges":"https://badges.roblox.com/",
		"Billing":"https://billing.roblox.com/",
		"Catalog":"https://catalog.roblox.com/",
		"CDN Provider":"https://cdnproviders.roblox.com/",
		"Chat":"https://chat.roblox.com/",
		"Client Settings":"https://clientsettings.roblox.com/",
		"Contacts":"https://contacts.roblox.com/",
		"Content Store":"https://contentstore.roblox.com/",
		"Develop":"https://develop.roblox.com/",
		"Economy":"https://economy.roblox.com/",
		"Engagement Payouts":"https://engagementpayouts.roblox.com/",
		"Followings":"https://followings.roblox.com/",
		"Friends":"https://friends.roblox.com/",
		"Game Internationalization":"https://gameinternationalization.roblox.com/",
		"Game Join":"https://gamejoin.roblox.com/",
		"Game Persistence":"https://gamepersistence.roblox.com/",
		"Games":"https://games.roblox.com/",
		"Groups":"https://groups.roblox.com/",
		"Groups Moderation":"https://groupsmoderation.roblox.com/",
		"Inventory":"https://inventory.roblox.com/",
		"Item Configuration":"https://itemconfiguration.roblox.com/",
		"Legacy":"https://api.roblox.com/",
		"Locale":"https://locale.roblox.com/",
		"Localization Tables":"https://localizationtables.roblox.com/",
		"Metrics":"https://metrics.roblox.com/",
		"Notifications":"https://notifications.roblox.com/",
		"Points":"https://points.roblox.com/",
		"Premiums Features":"https://premiumfeatures.roblox.com/",
		"Presence":"https://presence.roblox.com/",
		"Private Messages":"https://privatemessages.roblox.com/",
		"Publish":"https://publish.roblox.com/",
		"Economy creator stats":"https://economycreatorstats.roblox.com/",
		"Share":"https://share.roblox.com/",
		"Text Filter":"https://textfilter.roblox.com/",
		"Thumbnails":"https://thumbnails.roblox.com/",
		"Thumbnails Resizer":"https://thumbnailsresizer.roblox.com/",
		"Trades":"https://trades.roblox.com/",
		"Translation Roles":"https://translationroles.roblox.com/",
		"Translation":"https://translations.roblox.com/",
		"Two step Verification":"https://twostepverification.roblox.com/",
		"User Moderation":"https://usermoderation.roblox.com/",
		"Users":"https://users.roblox.com/",
		"Voice":"https://voice.roblox.com/",
		"Website":"https://roblox.com/",
		"Status Website":"https://status.roblox.com"
	}

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
app.run("0.0.0.0",port=80)