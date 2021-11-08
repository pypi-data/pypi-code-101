import requests
from . import server
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
	return logs

def statuscli(down='all'):
  if down == 'all':
    return '\n'.join(status())
  elif down == 'down':
    s = []
    for text in status():
      if "not working" in text:
        s.append(text)
    return '\n'.join(s)
  elif down == 'up':
    s = []
    for text in status():
      if "not working" not in text:
        s.append(text)
    return '\n'.join(s)
def statusserver(ip='0.0.0.0',port=80,usessl=False,ssl_context = 'adhoc'):
  if usessl:
    server.app.run(ip,port,ssl_context=ssl_context)
  else:
    server.app.run(ip,port)
    