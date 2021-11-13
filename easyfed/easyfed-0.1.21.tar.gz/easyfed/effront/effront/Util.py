import torch
import copy
import os
import crypten
import torch
import time

crypten.init()
import collections
from FModel.models import Clients
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
savefile=os.path.join(BASE_DIR, 'static', 'modelfile','clients.tsv')

import random
def randomcolor():
    colors=[]
    for _ in range(50):
        colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0,14)]
        colors.append("#"+color)
    return colors

#
alive_client={}
def setsession(key):
    s=time.time()
    alive_client[key]=s
def getsession(key):
    s=time.time()
    if key in alive_client:
        if (s-alive_client[key])>300:
            del alive_client[key]
    return alive_client.get(key,-1)
def getClients():
    clients=Clients.objects.all()
    print('clients',len(clients))
    clientsList=[]
    for cl in clients:
        item={}
        item['id']=cl.CID
        item['name']=cl.CName
        item['key']=cl.Key
        item['loss']='%.4f'%float(cl.Loss) if cl.Loss.strip() and float(cl.Loss)>0 else ''
        item['status']=cl.Status
        item['checked']='checked' if int(cl.Status)==1 else ''
        clientsList.append(item)
    return clientsList
def setClientStatus(key,status):
    result=0
    client=Clients.objects.filter(Key=key).first()
    if client:
        if client.Status!=int(status):
            client.Status=status
            client.save()
            result=1
    return result
def getClientId(cname,modeltype,key=None):
    context={}
    context['result']=0
    if not key or (key and not key.strip()):
        count=Clients.objects.count()
        key=getMD5('%s%s%s'%(count,cname,modeltype))
        ncl=Clients.objects.create(ModelType=modeltype,CName=cname,Key=key,Status=0)
        context['clientid']=ncl.CID
        context['key']=key 
        print(context)
    elif key and key.strip() and not Clients.objects.filter(Key=key).first():
        ncl=Clients.objects.create(ModelType=modeltype,CName=cname,Key=key,Status=0)
        context['clientid']=ncl.CID
        context['key']=key 
    elif Clients.objects.filter(Key=key,Status=1).first():
        context['result']=1
    return context
def average_weights(w):
    """
    Returns the average of the weights.
    """
    w_avg = copy.deepcopy(w[0])
    try:
        for key in w_avg.keys():
            for i in range(1, len(w)):
                w_avg[key]=w_avg[key].cpu()
                w_avg[key] +=w[i][key].cpu()
            w_avg[key] = torch.div(w_avg[key], len(w))
    except Exception as ex:
        print('please check model type or clean catch',ex)
    return w_avg

def average_weights_enc(w):
    """
    Returns the average of the weights.
    """
    new_w = collections.OrderedDict()
    w_avg = copy.deepcopy(w[0])
    try:
        for key in w_avg.keys():
            for i in range(1, len(w)):
                w_avg[key]=w_avg[key].cpu()
                w_avg[key] +=w[i][key].cpu()
            # w_avg[key] = torch.div(w_avg[key].get_plain_text(), len(w))
            new_w[key.replace('.data','')]=torch.div(w_avg[key].get_plain_text(), len(w))
    except Exception as ex:
        print('please check model type or clean catch',ex)
    return new_w

def check_fed_model(save_dir,keys,type,test_acc=None,test_loss=None,EpochCount=None):
    print('check_fed_model',save_dir,keys,type)
    # addtasklog(save_dir,clientnumber,taskname,'test_acc',test_acc,'test_loss',test_loss,_clientid)
    result=1
    cmodels=[]
    try:
        for key in keys:
            if os.path.exists(os.path.join(save_dir,key)):
                model=torch.load(os.path.join(save_dir,key))
                cmodels.append(model)
        if(len(keys)==len(cmodels)):
            result=3
    except Exception as es:
        print(es)
    if result==3:
        if type=='plain':
            avg_model=average_weights(cmodels)
        else:
            avg_model=average_weights_enc(cmodels)
        if avg_model:
            for key in keys:
                try:
                    if os.path.exists(os.path.join(save_dir,key)):
                        model=torch.load(os.path.join(save_dir,key))
                        torch.save(avg_model,os.path.join(save_dir,'%s_model'%(key)))
                        os.remove(os.path.join(save_dir,key))
                except:
                    pass
    return result
 
def check_client(save_dir,key):
    # addtasklog(save_dir,'Client_%s'%_clientid)
    result=0
    try:
        if os.path.exists(os.path.join(save_dir,key)):
            model=torch.load(os.path.join(save_dir,key))
            result=1
    except:
        pass
    return result
def check_client_all(save_dir,keys):
    # addtasklog(save_dir,'Client_%s'%_clientid)
    result=1
    try:
        for key in keys:
            print('start load',key)
            model=torch.load(os.path.join(save_dir,key))
            print('end load',key)
        result=3
    except:
        pass
    return result

import hashlib
 
def getMD5(message):
    m = hashlib.md5()
    m.update(message.encode(encoding='utf-8'))
    return m.hexdigest()