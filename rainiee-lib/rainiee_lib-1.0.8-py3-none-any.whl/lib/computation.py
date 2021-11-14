def daily_return_percentage(stock):
    if stock['pre_close_price'] == 0:
        return 1
    return stock['close_price'] / stock['pre_close_price']

def intraday_return_percentage(stock):
    return stock['close_price'] / stock['open_price']
