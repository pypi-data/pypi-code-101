try:
	import requests , os , sys , user_agent , json , secrets
	from user_agent import generate_user_agent
	
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	
class checkeml:
	
	def instagram(email):
		
		url = "https://www.instagram.com/accounts/login/ajax/"
		headers ={
        'authority': 'www.instagram.com',
        'method': 'POST',
        'path': '/accounts/login/ajax/',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
        'content-length': '277',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '7a3a3e64fa87',
        'x-requested-with': 'XMLHttpRequest'}
		
		data ={
        'username': str(email),
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'}
		
		response = requests.post(url, data=data, headers=headers)
		
		if ('"message":"There was an error with your request. Please try again."') in response.text:
			
			return True
		
		else:
			
			return False
			
	def facebook(email):
		
		url ="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(email)+"&locale=en_US&password=password&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
	   	
		
		response = requests.get(url)
		
		if ("The password you entered is incorrect. Please try again.") in response.text:
			
			return True
		
		else:
			
			return False
			
        
    
    
	def twitter(email):
		
		url = "https://twitter.com/users/email_available?email="
		headers = {
	    'Host': 'twitter.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'User-Agent': str(generate_user_agent()),
		'Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}
		
		data = {
        'account_sdk_source':'app', 
	    'email':str(email), 
	    'mix_mode':'1', 
	    'type':'31'}
		
		response = requests.get(f'{url}{email}',headers=headers)
		
		if ('"taken":false') in response.text:
			
			return False
		
		else:
			
			return True
			
	
	#print
	#print
	