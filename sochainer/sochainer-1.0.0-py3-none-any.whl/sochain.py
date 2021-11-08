import requests
from configparser import ConfigParser
from importlib import resources  # Python 3.7+

coins = ['BTC', 'DASH', 'ZEC', 'DOGE', 'LTC']

def get_prices():


    prices = {}
    for coin in coins:
        price = 0.00
        price_data = get_price(coin)
        for e in price_data['prices']:
            if e['exchange'] == 'binance':
                price = e['price']
                break
            else:
                # might as well just set price of other exchange
                price = e['price']
        prices[coin] = price

    return prices

def get_info(coin):
    if coin not in coins:
        raise Exception(coin+" is not supported. Please try BTC, DASH, ZEC, DOGE, LTC")

    cfg = ConfigParser()
    cfg.read_string(resources.read_text("sochainer", "config.cfg"))
    url = cfg.get("feed", "url")


    response = requests.get(url + 'get_info/'+coin)

    if response.status_code == 200:
        # everything went swimmingly
        # parse the response as JSON
        content = response.json()

        return content['data']
    else:
        raise Exception(response.json()['data'])


def get_price(coin):
    if coin not in coins:
        raise Exception(coin + " is not supported. Please try BTC, DASH, ZEC, DOGE, LTC")

    cfg = ConfigParser()
    cfg.read_string(resources.read_text("sochainer", "config.cfg"))
    url = cfg.get("feed", "url")

    response = requests.get(url + 'get_price/' + coin+"/USD")

    if response.status_code == 200:
        # everything went swimmingly
        # parse the response as JSON
        content = response.json()

        return content['data']
    else:
        raise Exception(response.json()['data'])