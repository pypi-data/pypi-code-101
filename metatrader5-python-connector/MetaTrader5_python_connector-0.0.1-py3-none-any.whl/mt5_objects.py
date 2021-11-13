from azure.storage.blob import BlobServiceClient
import pandas as pd 
from azure.storage.blob import BlobServiceClient
from datetime import datetime

class MT5_dataframe:

    def __init__(self,dataframe) -> None:
        
        self.dataframe = dataframe 

    def to_blob(self,constr,container,blob_path,file_type='csv'):
        
        blobservice = BlobServiceClient.from_connection_string(constr)

        df = self.dataframe
        if file_type == 'csv':
            file = df.to_csv()
            blob = blobservice.get_blob_client(container=container,
                                                blob=blob_path)
            blob.upload_blob(file,overwrite=True)
        
        elif file_type == 'parquet':
            file = df.to_parquet()
            blob =  blobservice.get_blob_client(container=container,
                                                blob=blob_path)
            blob.upload_blob(file, overwrite=True)

       

    def to_datetime(self):

        for col in self.dataframe.loc[:,self.dataframe.columns.str.contains('time')].columns:
            if 'msc' in col:
                self.dataframe[col] = pd.to_datetime(self.dataframe[col],unit='ms')
            else:
                self.dataframe[col] = pd.to_datetime(self.dataframe[col],unit='s')
        
        return (MT5_dataframe(self.dataframe))


class MT5_list:

    def __init__(self,list) -> None:
        
        self.list = list 
    
    def to_blob(self,constr, container, blob_path,disable_progress_bar=False):


        blobservice = BlobServiceClient.from_connection_string(constr)

        df_list = self.list 
        for df in tqdm(df_list,disable=disable_progress_bar):

            symbol = df.loc[0,'symbol']
            start  = df.loc[0,'time']
            end = df.loc[df.index[-1],'time']
            if start.year == datetime.now().year:
                blob = blobservice.get_blob_client(container=container,
                                            blob=blob_path+f'/{symbol} - {start} - .csv')
            else:
                blob = blobservice.get_blob_client(container=container,
                                                blob=blob_path+f'/{symbol} - {start} - {end}.csv')

            try:
                blob.upload_blob(df.to_csv(index=False),overwrite=True)
                # print(f'File uploaded to {container}/{blob_path}')
            except:
                pass
                print(f'Upload failed.\n {e}')





