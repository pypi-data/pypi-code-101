class Portfolio(object):
    def __init__(self, symbol : str, symbol_name : str, perc : str, ext = {}):
        self.symbol = symbol
        self.perc = perc
        self.ext = ext