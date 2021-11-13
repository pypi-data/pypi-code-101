from easyfed.utils.functions import *
import os
import time
import torch
class server():
    def __init__(self,bdir,port=16668):
        self.bdir=bdir
        self.port=port
    def run(self):
        path=os.path.join(self.bdir,'effront','manage.py')
        os.system("python %s migrate && python %s runserver 0.0.0.0:%s"%(path,path,self.port))

class client():
    def __init__(self,clientName,host,modeltype,type='plain'):
        self.clientname=clientName
        self.host=host
        self.modeltype=modeltype
        self.key=None
        self.type=type
    def login(self):
        result=client_login(self.host,self.clientname,self.modeltype)
        while int(result['result'])!=1:
            print('Client %s request to login.'%(self.clientname))
            result=client_login(self.host,self.clientname,self.modeltype)
            if int(result['result'])!=1:
                time.sleep(5)
        self.key=result['key']
        print('Client %s login successful.'%(self.clientname),'key',self.key)
    def submit(self,model,omodel=None,metric=None):
        if self.type=='plain' and omodel is None:
            omodel=model
        req=get_status(self.host,self.key,self.type,self.modeltype)
        state,clientstatus,url=req['result'],req['clientstatus'],req['modelurl']
        save_path='' 
        while int(state)!=0:
            if int(clientstatus)==0:
                send_model(self.host,self.key,self.type,self.modeltype,model,metric)
            req=get_status(self.host,self.key,self.type,self.modeltype)
            if int(req['clientstatus'])!=0:
                print('waiting for other clients...')
            state,clientstatus,url=req['result'],req['clientstatus'],req['modelurl']
            if url:
                save_path=download_model(self.host,req['modelurl'],self.key)
                break
            time.sleep(5)
        if save_path:
            mm=torch.load(save_path)
            omodel.load_state_dict(mm)
            print('model weights updated...')
        return omodel