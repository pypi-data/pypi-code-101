"""
Author      : Mauricio Tabares
Author_email: matabares@netactica.com
License     : MIT
"""
import os
import pathlib
from google.cloud import storage
from nos_parser.persistence_handler import PersistenceHandler


class GCSPersistence(PersistenceHandler):
    def __init__(self):
        self.client = storage.Client()
        self.blob_path = 'drain_state.bin'
        self.bucket_path = 'tel_nos_persistent'
        self.bucket=self.client.get_bucket(self.bucket_path);  
        
        
    def save_state(self,state):
        if storage.Blob(bucket=self.bucket, name=self.blob_path).exists(self.client):
            self.blob = self.bucket.get_blob(self.blob_path)
            pathlib.Path('state.bin').write_bytes(state)
            self.blob.upload_from_filename('state.bin')
            
        self.blob=self.bucket.blob(self.blob_path)
        pathlib.Path('state.bin').write_bytes(state)
        self.blob.upload_from_filename('state.bin')

    def load_state(self):
        if storage.Blob(bucket=self.bucket, name=self.blob_path).exists(self.client):
            self.blob = self.bucket.get_blob(self.blob_path)
            self.blob.download_to_filename('state.bin')
            return pathlib.Path('state.bin').read_bytes()

        return None
