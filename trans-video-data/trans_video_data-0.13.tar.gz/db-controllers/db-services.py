"""
@File: None
@Author: Jackpot
@Date: None
@Description: None
@email: wikileaks928@gmail.com
"""
from msilib import add_data

import grpc
import db_crud_pb2
import db_crud_pb2_grpc


class DbServer:
    def __init__(self):
        channel = grpc.insecure_channel("192.168.1.35:1998")
        self.stub = db_crud_pb2_grpc.DataServiceStub(channel)

    def get_data(self, keys, **kwargs):
        res = db_crud_pb2.SelParam(flag=1, Video=keys)
        features = self.stub.SelData(res)
        return features

    def add_data(self, video_name, video_path, video_info_path, video_trans_path):
        res = db_crud_pb2.AddParam(VideoName=video_name, VideoPath=video_path, VideoInfoPath=video_info_path, VideoTransPath=video_trans_path)
        features = self.stub.AddData(res)
        return features

    def mod_data(self, key, values):
        pass
