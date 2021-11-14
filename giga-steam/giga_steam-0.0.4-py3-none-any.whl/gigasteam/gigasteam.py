import time
import json
import logging
import requests
import rsa
import hmac
import base64
import struct
import hashlib
from random import randint
from hashlib import sha1
import lxml
from bs4 import BeautifulSoup

class Steam:
    def __init__(self, username: str, password: str, shared_secret: str=None):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.baseURL = "https://steamcommunity.com"
        self.shared_secret = shared_secret
        self.steamid = None
        self.token_secure = None
        self.webcookie = None
        
        logging.basicConfig(level=logging.INFO, format=f"%(asctime)s | %(levelname)s | {self.username} | %(message)s")
        logging.getLogger("requests").setLevel(logging.WARNING)

        self.accounts = self.loadAccounts()
        self.user = self.accounts[username] if username in self.accounts else None

    def request(self, type_: str, url: str, data=None, params=None, headers=None):
        tries = 1
        while tries <= 5:
            tries += 1
            if type_ == 'get':
                res = self.session.get(self.baseURL + url, params=params, headers=headers, data=data)
            elif type_ == 'post':
                res = self.session.post(self.baseURL + url, params=params, headers=headers, data=data)
            
            if res and res.status_code == 200:
                return res
            elif res and res.status_code == 429:
                logging.error("Too many requests to " + url)
                time.sleep(tries * 5)
            elif res and res.status_code == 500:
                logging.error(res.json())
            else:
                print(res.status_code, res.content)
                return None

    def getSoup(self, url: str):
        return BeautifulSoup(self.request('get', url).content, 'lxml')

    def loadAccounts(self):
        try:
            with open('accounts.json') as f:
                return json.load(f)
        except:
            return {}

    def getRSA(self) -> dict:
        data = { "username": self.username }
        res = self.request(type_='post', url='/login/getrsakey/', data=data).json()
        rsa_mod = int(res['publickey_mod'], 16)
        rsa_exp = int(res['publickey_exp'], 16)
        rsa_timestamp = res['timestamp']
        return {'rsa_key': rsa.PublicKey(rsa_mod, rsa_exp), 'rsa_timestamp': rsa_timestamp}

    def encryptRSA(self, rsa_params: dict) -> str:
        return base64.b64encode(rsa.encrypt(self.password.encode('utf-8'), rsa_params['rsa_key']))

    def getTwoFactorCode(self) -> str:
        if (not self.user and not self.shared_secret) or (self.user and 'shared_secret' not in self.user): return None
        shared_secret = self.shared_secret if self.shared_secret else self.user['shared_secret']
        timestamp = int(time.time())
        time_buffer = struct.pack('>Q', timestamp // 30)
        time_hmac = hmac.new(base64.b64decode(shared_secret), time_buffer, digestmod=sha1).digest()
        begin = ord(time_hmac[19:20]) & 0xf
        full_code = struct.unpack('>I', time_hmac[begin:begin + 4])[0] & 0x7fffffff
        chars = '23456789BCDFGHJKMNPQRTVWXY'
        code = ''
        for _ in range(5):
            full_code, i = divmod(full_code, len(chars))
            code += chars[i]
        return code

    def login(self):
        rsaParams = self.getRSA()
        data = {
            "username": self.username,
            "password": self.encryptRSA(rsaParams),
            "twofactorcode": self.getTwoFactorCode(),
            "captchagid": -1,
            "rsatimestamp": rsaParams['rsa_timestamp']
        }
        res = self.request('post', '/login/dologin/', data=data).json()
        if res['success']:
            self.steamid = res['transfer_parameters']['steamid']
            self.token_secure = res['transfer_parameters']['token_secure']
            self.webcookie = res['transfer_parameters']['webcookie']
            return True
        else:
            if 'requires_twofactor' in res:
                logging.error("Two factor authentication required")
            else:
                print(res)
            return False

    def getInventory(self, gameID: str, steamID: str = None) -> dict:
        params = {
            "l": "english",
            "count": 150
        }
        return self.request('get', f"/inventory/{steamID if steamID else self.steamid}/{gameID}/2?", params=params).json()

    def getTradableItem(self, inventory: dict) -> dict:
        if 'assets' not in inventory: return None
        for asset, desc in zip(inventory['assets'], inventory['descriptions']):
            if 'tradable' in desc and desc['tradable'] == 1: return {**asset, **desc}
        return None

    def getTradableItems(self, inventory: dict) -> list:
        if 'assets' not in inventory: return None
        items = []
        for asset, desc in zip(inventory['assets'], inventory['descriptions']):
            if 'tradable' in desc and desc['tradable'] == 1: items.append({**asset, **desc})
        return items
    
    def createOffer(self, items: list) -> dict:
        return {
            "assets": [
                {
                    "appid": item['appid'],
                    "contextid":"2",
                    "amount": 1,
                    "assetid": item['assetid']
                } for item in items],
            "currency": [],
            "ready": True
        }

    def createEmptyOffer(self) -> dict:
        return {"assets":[],"currency":[],"ready": False}

    def sendTradeOffer(self, steamID: str, me: dict, them: dict, offerMessage=""):
        offer = {
            "newversion": True,
            "version": 2,
            "me": me,
            "them": them
        }

        data = {
            'sessionid': self.session.cookies.get_dict()['sessionid'],
            'serverid': '1',
            'partner': steamID,
            'tradeoffermessage': offerMessage,
            'json_tradeoffer': json.dumps(offer),
            'captcha': '',
            'trade_offer_create_params': '{}'
        }
        
        headers = {
            'Referer': "https://steamcommunity.com/tradeoffer/new/?partner=219864806",
            'Origin': 'https://steamcommunity.com',
        }
        
        res = self.request('post', '/tradeoffer/new/send', data=data, headers=headers)
        return res.json()
    
    def acceptTradeOffer(self, steamID: str, tradeID: str):
        data = {
            'sessionid': self.session.cookies.get_dict()['sessionid'],
            'serverid': '1',
            'partner': steamID,
            'tradeofferid': tradeID,
            "captcha": ""
        }
        headers = {'Referer': f"https://steamcommunity.com/tradeoffer/{tradeID}"}
        return self.request('post', f'/tradeoffer/{tradeID}/accept', data=data, headers=headers).json()
    
    def confirmTrade(self, tradeid: str):
        confirmations = []
        params = self.createParams(self.user, 'conf')
        res = self.request('get', '/mobileconf/conf', params=params)
        soup = BeautifulSoup(res.content, 'html.parser')
        confirmations = [{
            "id": confirmation['data-confid'],
            "data_confid": confirmation['data-confid'],
            "data_key": confirmation['data-key']
        } for confirmation in soup.find('div', id='mobileconf_list').findAll('div', class_="mobileconf_list_entry")]
        for confirmation in confirmations:
            tag = 'details' + confirmation['id']
            params = self.createParams(self.user, tag)
            res = self.request('get', '/mobileconf/details/' + confirmation['id'], params=params).json()
            soup = BeautifulSoup(res['html'], 'html.parser')
            confirmation_id = soup.select('.tradeoffer')[0]['id'].split('_')[1]
            if str(confirmation_id) == str(tradeid):
                tag = 'allow'
                params = self.createParams(self.user, tag)
                params['op'] = tag
                params['cid'] = confirmation['data_confid']
                params['ck'] = confirmation['data_key']
                headers = {'X-Requested-With': 'XMLHttpRequest'}
                return self.request('get', "/mobileconf/ajaxop", params=params, headers=headers).json()

    def createParams(self, account: dict, tag: str) -> dict:
        timestamp = int(time.time())
        hexed_steam_id = sha1(str(self.user['steam_id']).encode('ascii')).hexdigest()
        confirmation_key =  base64.b64encode(hmac.new(base64.b64decode(self.user['identity_secret']), struct.pack('>Q', timestamp) + tag.encode('ascii'), digestmod=sha1).digest())
        android_id = 'android:' + '-'.join([hexed_steam_id[:8], hexed_steam_id[8:12], hexed_steam_id[12:16], hexed_steam_id[16:20], hexed_steam_id[20:32]])
        return {'p': android_id,
                'a': self.user['steam_id'],
                'k': confirmation_key,
                't': timestamp,
                'm': 'android',
                'tag': tag
        }

    def cancelAllTradeOffers(self):
        data = {'sessionid': self.user.session_id} if "sessionid" in self.user else None
        for trade_offer in self.getAllSentOffers():
            res = self.request('post', f"/tradeoffer/{trade_offer['trade_id']}/cancel", data=data).json()
            if res['tradeofferid'] == trade_offer['trade_id']:
                logging.info(f"Trade offer {trade_offer['trade_id']} canceled")
            else:
                logging.error(f"Failed to cancel trade offer {trade_offer['trade_id']} Error: {res}")

    def getAllSentOffers(self) -> list: #returns a list of trade offers' dicts
        trade_offers = []
        res = self.request('get', f'/profiles/{self.user["steam_id"]}/tradeoffers/sent/')
        soup = BeautifulSoup(res.content, 'lxml')
        for trade_offer in soup.findAll(class_='tradeoffer'):
            #sender items
            sender_items = trade_offer.findAll(class_='tradeoffer_item_list')[0].findAll(class_='trade_item')
            sender_items_list = []
            for item in sender_items:
                try:
                    _, gameID, classID, instanceID = item['data-economy-item'].split('/')
                except:
                    _, gameID, classID = item['data-economy-item'].split('/')
                    instanceID=None
                sender_items_list.append(
                    {"gameID": gameID, "classID": classID, "instanceID":instanceID, "image_url": item.img['src']}
                )
            #receiver items
            receiver_items = trade_offer.findAll(class_='tradeoffer_item_list')[1].findAll(class_='trade_item')
            receiver_items_list = []
            for item in receiver_items:
                try:
                    _, gameID, classID, instanceID = item['data-economy-item'].split('/')
                except:
                    _, gameID, classID = item['data-economy-item'].split('/')
                    instanceID=None
                receiver_items_list.append(
                    {"gameID": gameID, "classID": classID, "instanceID":instanceID, "image_url": item.img['src']}
                )
            
            trade_offers.append({
                "trade_id": trade_offer['id'].strip('tradeofferid_'),
                "receiver_id": trade_offer.find(class_='tradeoffer_items secondary').find(class_='tradeoffer_avatar')['href'].split('/')[-1],
                "receiver_id_short": trade_offer.find(class_='tradeoffer_items secondary').find(class_='tradeoffer_avatar')['data-miniprofile'],
                "sender_items": sender_items_list,
                "receiver_items": receiver_items_list,
            })
        return trade_offers