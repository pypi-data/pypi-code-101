import requests
import json
class Token:
    def __init__(self,UserApiKey,SecretKey):
        self.UserApiKey=UserApiKey
        self.SecretKey=SecretKey

    def get_token(self):
        url ='http://RestfulSms.com/api/Token'
        headers = {
        "Content-Type": "application/json",
        }
        body = {
        "UserApiKey": self.UserApiKey,
        "SecretKey": self.SecretKey
        }
        response = requests.post(url, data=json.dumps(body), headers=headers)
        if response.status_code is 201:
            if response.json()['IsSuccessful'] is True:
                secure_token = response.json()['TokenKey']
                return secure_token
        return None

    def get_credit(self):
        url ='http://RestfulSms.com/api/credit'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': self.get_token()
        }
        response = requests.get(url, headers=headers)
        return response
    