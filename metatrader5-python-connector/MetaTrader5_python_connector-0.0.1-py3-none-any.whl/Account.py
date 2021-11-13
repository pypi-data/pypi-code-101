# from src.MT5app import MT5app 
from .mt5_objects import MT5_dataframe, MT5_list 
import pandas as pd 
from datetime import date, datetime

class Account():

    def __init__(self, client, account_id):
        
        # self.app = MT5app(account_id=account_id,password=password,server=server)
        self.account_id = account_id
        self.client = client

    def get_account_info(self):
        
        account_info = self.client.account_info()._asdict()
        account_info_df = pd.DataFrame(account_info,index=[datetime.now()])
        
        return MT5_dataframe(account_info_df)
        
    def get_positions(self):
        
        df_list = [] 

        for position in (self.client.positions_get()):

            df = pd.DataFrame(position._asdict(),index=[datetime.now()])
            df['account_id'] = self.account_id
            df_list.append(df)
        
        positions = pd.concat(df_list)
        
        return MT5_dataframe(positions).to_datetime() 
    
    def get_deals(self):
        
        deals = self.client.history_deals_get(datetime(2010,1,1),datetime.now())
        deal_keys = deals[0]._asdict().keys()
        deals_df = pd.DataFrame(deals,
                               columns=deal_keys,
                               index=[datetime.now() for i in range(len(deals))])
        deals_df['account_id'] = self.account_id
        newDict = dict(filter(lambda elem: 'DEAL_TYPE' in elem[0] , self.client.__dict__.items()))
        inv_map = {v: k for k, v in newDict.items()}

        deals_df['type_descr'] = deals_df['type'].map(inv_map)
        
        return MT5_dataframe(deals_df).to_datetime()