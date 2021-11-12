import phonenumbers
import requests
import json
import smtplib

def format_number(number):
	number = '+'+str(number)
	return number

def validate_number(formatted_number):
	x = phonenumbers.parse(formatted_number)
	if phonenumbers.is_valid_number(x):
		return (True, { 'valid_number':formatted_number })

def get_number_info(vaild_number):
	if vaild_number[0]:
		number_to_url = vaild_number[1]['valid_number'].split("+")[1]
		url = 'https://api.telnyx.com/v1/phone_number/'+number_to_url
		site_data = requests.get(url).text
		data = {
			'phone_number': number_to_url,
			'country_code': json.loads(site_data)['country_code'],
			'national_format': json.loads(site_data)['national_format'],
			'phone_carrier': json.loads(site_data)['carrier']['name'],
			'phone_type': json.loads(site_data)['carrier']['type']
		}
	return data

def create_profile(username, password):
	profile = {
		"profile": {
			"login_info": {
				"username": username,
				"password": password
			}
		}
	}
	return profile

class Operator:
	def __self__(self):
		pass

	def provider_list(self):
		providers = {
			'Verizon': 'vs',
			'BoostMobile': 'bm',
			'AT&T': 'att',
			'CricketWireless': 'cw',
			'C-Spire': 'cs',
			'ConsumerCellular': 'cc',
			'MetroPCS': 'mp',
			'MintMobile': 'mm',
			'Sprint': 's',
			'StraightTalk': 'st',
			'T-Mobile': 'tm',
			'XfinityMobile': 'xm'
		}

		return providers

	def provider(self,provider_code):
		providers = {
			'vs': 'vtext.com',
			'bm': 'vtext.com',
			'att': 'txt.att.net',
			'cw': 'sms.cricketwireless.net',
			'cs': 'cspire1.com',
			'cc': 'mailmymobile.net',
			'mp': 'mymetropcs.com',
			'mm': 'mailmymobile.net',
			's': 'messaging.sprintpcs.com',
			'st': 'vtext.com',
			'tm': 'tmomail.net',
			'xm': 'vtext.com'
		}

		for provider in providers:
			if provider_code == provider:
				return providers[provider_code]
				break

	def send_sms_to(self, recv_number, profile, provider, message):
		recv_email = f'{str(recv_number)}@{provider}'

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(profile['profile']['login_info']['username'], profile['profile']['login_info']['password'])
		s.sendmail(profile['profile']['login_info']['username'], recv_email, message)
		s.close()
		return '[XOR] Message Sent!'
		
	def send_email_to(self, recv_email, profile, message):
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(profile['profile']['login_info']['username'], profile['profile']['login_info']['password'])
		s.sendmail(profile['profile']['login_info']['username'], recv_email, message)
		s.close()
		return '[XOR] Email Sent!'