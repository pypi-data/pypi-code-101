import MetaTrader5 as mt5
from .Account import Account
from .Price import Price

class MT5app():
    def __init__(self,account_id,password,server,path):
        self.account_id = account_id 
        self.password = password
        self.server = server 
        self.path = path 

        

        print(self.account_id)
        # if not mt5.initialize(path=os.path.dirname(__file__)+"\\MetaTrader 5\\terminal64.exe",login=self.account_id,password=self.password,server=self.server):
        if not mt5.initialize(path=self.path,login=self.account_id,password=self.password,server=self.server):    
            print("initialize() failed, error code =",mt5.last_error())
            mt5.shutdown()
        
        
        self.client = mt5 

        self.Price = Price(self.client)
        self.Account = Account(self.client,self.account_id)

        self.timeframes = self.Price.get_timeframes()
        self.symbols = self.Price.get_symbols()


    
