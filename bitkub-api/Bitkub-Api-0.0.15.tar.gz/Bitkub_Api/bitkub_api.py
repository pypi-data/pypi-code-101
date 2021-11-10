import requests
import json
import hashlib
import hmac
import time


#  all output are json except for the servertime function is integer


# GET v #######################################################################################################################################################
class Bitkub:
    def __init__(self, api_key: str, api_secret: bytes):  # key and secret
        self._key = api_key
        self._se = api_secret

    def status(self):  # get status
        url = "https://api.bitkub.com/api/status"
        response = requests.get(url).json()
        return response

    def servertime(self):  # get server time
        response = int(time.time())
        return response

    def symbols(self):  # get symbols
        url = "https://api.bitkub.com/api/market/symbols"
        response = requests.get(url).json()
        return response

    def ticker(self, sym: str = None):  # get ticker
        url = "https://api.bitkub.com/api/market/ticker?"
        response_url = url

        if sym is not None:
            sym = str.upper(sym)
            response_url = response_url + f"sym={sym}&"
        response = requests.get(response_url).json()
        return response

    def trades(self, sym: str, lmt: int):  # get trades
        url = "https://api.bitkub.com/api/market/trades?"
        response_url = url

        lmt = str(lmt)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&lmt={lmt}"
        response = requests.get(response_url).json()
        return response

    def bids(self, sym: str, lmt: int):  # get bids
        url = "https://api.bitkub.com/api/market/bids?"
        response_url = url

        lmt = str(lmt)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&lmt={lmt}"
        response = requests.get(response_url).json()
        return response

    def asks(self, sym: str, lmt: int):  # get asks
        url = "https://api.bitkub.com/api/market/asks?"
        response_url = url

        lmt = str(lmt)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&lmt={lmt}"
        response = requests.get(response_url).json()
        return response

    def books(self, sym: str, lmt: int):  # get books
        url = "https://api.bitkub.com/api/market/books?"
        response_url = url

        lmt = str(lmt)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&lmt={lmt}"
        response = requests.get(response_url).json()
        return response

    def tradingview(self, sym: str, Int: int, frm: int, to: int):  # get tradingview
        url = "https://api.bitkub.com/api/tradingview/history?"
        response_url = url

        Int = str(Int)
        frm = str(frm)
        to = str(to)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&int={Int}&frm={frm}&to={to}"
        response = requests.get(response_url).json()
        return response

    def depth(self, sym: str, lmt: int):  # get depth
        url = "https://api.bitkub.com/api/market/depth?"
        response_url = url

        lmt = str(lmt)
        sym = str.upper(sym)
        response_url = response_url + f"sym={sym}&lmt={lmt}"
        response = requests.get(response_url).json()
        return response

    # GET ^ #######################################################################################################################################################

    # POST encode sign v ##########################################################################################################################################
    def _json_encode(self, data):
        return json.dumps(data, separators=(',', ':'), sort_keys=True)

    def _sign(self, data, api_secret):
        j = self._json_encode(data)
        h = hmac.new(api_secret, msg=j.encode(), digestmod=hashlib.sha256)
        return h.hexdigest()

    def _get_header(self):
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-BTK-APIKEY': self._key,
        }
        return header

    def _sig_data(self, data):
        signature = self._sign(data, self._se)
        data['sig'] = signature
        return data

    # POST encode sign ^ ##########################################################################################################################################

    # POST v ######################################################################################################################################################

    def wallet(self, ts: int = None):  # get wallet
        url = "https://api.bitkub.com/api/market/wallet"

        data = {}
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def balances(self, ts: int = None):  # get balances
        url = "https://api.bitkub.com/api/market/balances"

        data = {}
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def place_bid(self, sym: str, amt: float, rat: float, typ: str, client_id: str = None, ts: int = None):  # place-bid
        url = "https://api.bitkub.com/api/market/place-bid"

        sym = str.upper(sym)
        typ = str.lower(typ)
        if typ == "market":
            rat = 0
        data = {
            'sym': sym,
            'amt': amt,
            'rat': rat,
            'typ': typ,
        }
        if client_id is not None:
            data.update({'client_id': client_id})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def place_bid_test(self, sym: str, amt: float, rat: float, typ: str, client_id: str = None, ts: int = None):  # place-bid(test)
        url = "https://api.bitkub.com/api/market/place-bid/test"

        sym = str.upper(sym)
        typ = str.lower(typ)
        data = {
            'sym': sym,
            'amt': amt,
            'rat': rat,
            'typ': typ,
        }
        if client_id is not None:
            data.update({'client_id': client_id})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def place_ask(self, sym: str, amt: float, rat: float, typ: str, client_id: str = None, ts: int = None):  # place-ask
        url = "https://api.bitkub.com/api/market/place-ask"

        sym = str.upper(sym)
        typ = str.lower(typ)
        if typ == "market":
            rat = 0
        data = {
            'sym': sym,
            'amt': amt,
            'rat': rat,
            'typ': typ,
        }
        if client_id is not None:
            data.update({'client_id': client_id})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def place_ask_test(self, sym: str, amt: float, rat: float, typ: str, client_id: str = None, ts: int = None):  # place-ask(test)
        url = "https://api.bitkub.com/api/market/place-ask/test"

        sym = str.upper(sym)
        typ = str.lower(typ)
        data = {
            'sym': sym,
            'amt': amt,
            'rat': rat,
            'typ': typ,
        }
        if client_id is not None:
            data.update({'client_id': client_id})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response


    def place_ask_by_fiat(self, sym: str, amt: float, rat: float, typ: str, ts: int = None):  # place-ask-by-fiat
        url = "https://api.bitkub.com/api/market/place-ask-by-fiat"

        sym = str.upper(sym)
        typ = str.lower(typ)
        data = {
            'sym': sym,
            'amt': amt,
            'rat': rat,
            'typ': typ,
        }
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def cancel_order(self, sym: str = None, id: int = None, sd: str = None, hash: str = None, ts: int = None):  # cancel order
        url = "https://api.bitkub.com/api/market/cancel-order"

        data = {}
        if hash is not None:
            data.update({'hash': hash})
        else:
            if sym or id or sd is None:
                raise Exception("sym, id, sd is required or use hash inserted")
            else:
                sym = str.upper(sym)
                data.update({'sym': sym, 'id': id, 'sd': sd})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def my_open_orders(self, sym: str, ts: int = None):  # get your open orders
        url = "https://api.bitkub.com/api/market/my-open-orders"

        sym = str.upper(sym)
        data = {
            'sym': sym,
        }
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def my_order_history(self, sym: str, p: int = None, lmt: int = None, start: int = None, end: int = None, ts: int = None):  # get your order history
        url = "https://api.bitkub.com/api/market/my-order-history"

        sym = str.upper(sym)
        data = {
            'sym': sym,
        }
        if p is not None:
            data.update({'p': p})
        if lmt is not None:
            data.update({'lmt': lmt})
        if start is not None:
            data.update({'start': start})
        if end is not None:
            data.update({'end': end})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def order_info(self, sym: str = None, id: int = None, sd: str = None, hash: str = None, ts: int = None):  # get order info
        url = "https://api.bitkub.com/api/market/order-info"

        data = {}
        if hash is not None:
            data.update({'hash': hash})
        else:
            if sym or id or sd is None:
                raise Exception("sym, id, sd is required or use hash inserted")
            else:
                sym = str.upper(sym)
                data.update({'sym': sym, 'id': id, 'sd': sd})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header(),
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_addresses(self, p: int = None, lmt: int = None, ts: int = None):  # get all crypto addresses
        url = "https://api.bitkub.com/api/crypto/addresses?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_withdraw(self, cur: str, amt: float, adr: str, mem: str = None, ts: int = None):  # withdraw crypto
        url = "https://api.bitkub.com/api/crypto/withdraw"

        cur = str.upper(cur)
        data = {
            'cur': cur,
            'amt': amt,
            'adr': adr,
        }
        if mem is not None:
            data.update({'mem': mem})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_internal_withdraw(self, cur: str, amt: float, adr: str, mem: str = None, ts: int = None):  # withdraw crypto internal
        url = "https://api.bitkub.com/api/crypto/internal-withdraw"

        cur = str.upper(cur)
        data = {
            'cur': cur,
            'amt': amt,
            'adr': adr,
        }
        if mem is not None:
            data.update({'mem': mem})
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_deposit_history(self, p: int = None, lmt: int = None, ts: int = None):  # get all crypto deposit history
        url = "https://api.bitkub.com/api/crypto/deposit-history?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_withdraw_history(self, p: int = None, lmt: int = None, ts: int = None):  # get all crypto withdraw history
        url = "https://api.bitkub.com/api/crypto/withdraw-history?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def crypto_generate_address(self, sym: str, ts: int = None):  # generate crypto address
        url = "https://api.bitkub.com/api/crypto/generate-address"

        sym = str.upper(sym)
        data = {
            'sym': sym,
        }
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def fiat_accounts(self, p: int = None, lmt: int = None, ts: int = None):  # get all fiat accounts
        url = "https://api.bitkub.com/api/fiat/accounts?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def fiat_withdraw(self, id: str, amt: float, ts: int = None):  # withdraw to bank
        url = "https://api.bitkub.com/api/fiat/withdraw"

        data = {
            'id': id,
            'amt': amt,
        }
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def fiat_deposit_history(self, p: int = None, lmt: int = None, ts: int = None):  # get all deposit history
        url = "https://api.bitkub.com/api/fiat/deposit-history?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def fiat_withdraw_history(self, p: int = None, lmt: int = None, ts: int = None):  # get all withdraw history
        url = "https://api.bitkub.com/api/fiat/withdraw-history?"
        response_url = url

        data = {}
        if p is not None:
            p = str(p)
            response_url = response_url + f"p={p}&"
        if lmt is not None:
            lmt = str(lmt)
            response_url = response_url + f"lmt={lmt}&"
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(response_url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def wstoken(self, ts: int = None):  # get wstoken
        url = "https://api.bitkub.com/api/market/wstoken"

        data = {}
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def user_limits(self, ts: int = None):  # get user limits
        url = "https://api.bitkub.com/api/user/limits"

        data = {}
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response

    def user_trading_credits(self, ts: int = None):  # get user trading credits
        url = "https://api.bitkub.com/api/user/trading-credits"

        data = {}
        if ts is not None:
            data.update({'ts': ts})
        else:
            data.update({'ts': self.servertime()})

        response = requests.post(url, headers=self._get_header,
                                 data=self._json_encode(self._sig_data(data))).json()
        return response


class Check:
    def check(self, response):
        if type(response) == int:
            return response
        codes = {
            0: 'No error',
            1: 'Invalid JSON payload',
            2: 'Missing X - BTK - APIKEY',
            3: 'Invalid API _key',
            4: 'API pending for activation',
            5: 'IP not allowed',
            6: 'Missing / invalid signature',
            7: 'Missing timestamp',
            8: 'Invalid timestamp',
            9: 'Invalid user',
            10: 'Invalid parameter',
            11: 'Invalid symbol',
            12: 'Invalid amount',
            13: 'Invalid rate',
            14: 'Improper rate',
            15: 'Amount too low',
            16: 'Failed to get balance',
            17: 'Wallet is empty',
            18: 'Insufficient balance',
            19: 'Failed to insert order into db',
            20: 'Failed to deduct balance',
            21: 'Invalid order for cancellation',
            22: 'Invalid side',
            23: 'Failed to update order status',
            24: 'Invalid order for lookup',
            25: 'KYC level 1 is required to proceed',
            30: 'Limit exceeds',
            40: 'Pending withdrawal exists',
            41: 'Invalid currency for withdrawal',
            42: 'Address is not in whitelist',
            43: 'Failed to deduct crypto',
            44: 'Failed to create withdrawal record',
            45: 'Nonce has to be numeric',
            46: 'Invalid nonce',
            47: 'Withdrawal limit exceeds',
            48: 'Invalid bank account',
            49: 'Bank limit exceeds',
            50: 'Pending withdrawal exists',
            51: 'Withdrawal is under maintenance',
            90: 'Server error (please contact support)',
        }
        if response.keys().__contains__('error'):
            code = response['error']
        else:
            return response
        if codes.keys().__contains__(code):
            response["code description"] = codes[code]
        return response
