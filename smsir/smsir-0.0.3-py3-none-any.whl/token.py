import requests
import json
class Token:
    def __init__(self,UserApiKey,SecretKey):
        self.UserApiKey=UserApiKey
        self.SecretKey=SecretKey
    def get_secure_token(self):
        headers = {
        "Content-Type": "application/json",
        }
        body = {
        "UserApiKey": self.UserApiKey,
        "SecretKey": self.SecretKey
        }
        response = requests.post('http://RestfulSms.com/api/Token', data=json.dumps(body), headers=headers)
        if response.status_code is 201:
            if response.json()['IsSuccessful'] is True:
                secure_token = response.json()['TokenKey']
                return secure_token
        return None
            