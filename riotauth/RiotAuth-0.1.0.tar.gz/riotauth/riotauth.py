import json
import re
import requests
from requests.sessions import Session


class riotauth():

    def __init__(self, username, password):
        print(username, password)
        self.user = username
        self.pwd = password
        self.sess = requests.Session()

    def getCookie(self):
        headers = {}
        headers['Content-Type'] = 'application/json'
        body = json.dumps({"client_id": "play-valorant-web-prod", "nonce": "1", "redirect_uri": "https://playvalorant.com/opt_in", "response_type": "token id_token"
                           })
        response = self.sess.post(
            "https://auth.riotgames.com/api/v1/authorization", data=body, headers=headers)
        return(response.json())

    def getToken(self):
        headers = {}
        data = json.dumps({
            "type": "auth",
            "username": self.user,
            "password": self.pwd,
            "remember": False,
            "language": "en_US"
        })
        headers['Content-Type'] = 'application/json'
        try:
            response = self.sess.put(
                "https://auth.riotgames.com/api/v1/authorization", data=data, headers=headers)
            cap = response.json()
            ggwp = re.split('#|&', cap['response']['parameters']['uri'])
            ggez = (ggwp[1]).split("=")
            print("Succesfully Logged In")
            return (self.sess)
        except KeyError:
            print("Credentials Invalid")


def RiotAuth(username, password):
    RA = riotauth(username, password)
    RA.getCookie()
    return(RA.getToken())
