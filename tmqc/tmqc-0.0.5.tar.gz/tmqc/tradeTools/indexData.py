# -*- coding: utf-8 -*-
import grpc
import sys
sys.path.append("./")
from tradeTools import indexData_pb2,indexData_pb2_grpc
from google.protobuf.json_format import MessageToJson
import json
import better_exceptions
import time
better_exceptions.hook()

HOST = "localhost"
HOST = "113.31.119.58"
PORT = 50052

def getIndexSymbols(dateTime = 20100118,indexID = "000300",):
    while 1:
        try:
            with grpc.insecure_channel(f"{HOST}:{PORT}") as channel:
                stub = indexData_pb2_grpc.indexDataStub(channel)

                print("=====【rpc】 getSymbols==========")
                sReq = json.dumps({
                    "indexID":indexID, "dateTime":int(dateTime)})
                response = stub.getSymbols(indexData_pb2.JSONRequest(sReq=sReq))
                jsonRsp = MessageToJson(response)
                jsonRsp = json.loads(jsonRsp)
                return jsonRsp["symbol"]
        except Exception as e:
            print(e)
            time.sleep(3)

if __name__ == '__main__':
    # logging.basicConfig()
    symbols500 = getIndexSymbols()
    print(symbols500)
    symbols300 = getIndexSymbols(indexID="000300")
    # print(symbols300)
    # d = list(set(symbols300)&set(symbols500))
    # print(len(d))