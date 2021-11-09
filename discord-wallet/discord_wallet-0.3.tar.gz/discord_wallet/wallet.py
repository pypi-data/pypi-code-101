import requests

def change_wallet_balance(botID, userID, amountOfCurrency, negative, symbol):
    url = 'https://discord-wallet.glitch.me/r'
    data = {
        'userID': userID,
        'clientID': botID,
        'amountOfCurrency': amountOfCurrency,
        'type': 'WITHDRAWAL' if negative == True else 'DEPOSIT',
        'symbol': symbol
    }
    x = requests.post(url, data)
    res = x.json()
    return res["response"]

def add_to_wallet(botID, userID, amountOfCurrency, symbol):
    return change_wallet_balance(botID, userID, amountOfCurrency, False, symbol)

def remove_from_wallet(botID, userID, amountOfCurrency, symbol):
    return change_wallet_balance(botID, userID, amountOfCurrency, True, symbol)

def check_balance(botID, userID, symbol):
    url = 'https://discord-wallet.glitch.me/r'
    data = {
        'userID': userID,
        'clientID': botID,
        'type': 'INQUIRY',
        'symbol': symbol
    }
    x = requests.post(url, data)
    res = x.json()
    return res["response"]