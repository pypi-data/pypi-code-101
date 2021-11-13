from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_exempt
import json
import os
import torch
from . import Util
from FModel.models import Clients
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_dir=os.path.join(BASE_DIR, 'static', 'modelfile')
colors=Util.randomcolor()
def log_in(func):
    def wrapper(request,*args,**kwargs):
        return  func(request,*args, **kwargs)
    return wrapper
@log_in
def index(request,context={}): 
    clients=Clients.objects.all()
    print('client count',len(clients))
    clientsList=[]
    for cl in clients:
        item={}
        item['id']=cl.CID
        item['name']=cl.CName
        item['key']=cl.Key
        item['ModelType']=cl.ModelType
        item['loss']='%.4f'%float(cl.Loss) if cl.Loss.strip() and float(cl.Loss)>0 else ''
        item['status']=cl.Status
        item['checked']='checked' if int(cl.Status)==1 else ''
        item['color']='green' if Util.getsession(cl.Key)>0 else 'blue'
        item['bgcolor']='background:%s'%(colors[int(cl.ModelType)])
        check=1 if os.path.exists(os.path.join(save_dir,'%s_modelb'%(cl.Key))) else 0
        item['check_model_file']=check
        item['down']='/download?key=%s'%cl.Key if check==1 else '#'
        clientsList.append(item)
    context['clients']=clientsList
    context['clients_count']=len(context['clients'])
    return render(request, 'index.html', context)
@csrf_exempt
@log_in
def client_login(request,context={}): 
    if request.method == 'POST':
        cname=request.POST.get('clientName')
        key=request.POST.get('key')
        modeltype=int(request.POST.get('modeltype'))
        print(cname,context)
        context=Util.getClientId(cname,modeltype,key)
        context['logggin']=1
        Util.setsession(key)
        # request.session.modified = True
    return HttpResponse(json.dumps(context),content_type="application/json")
@csrf_exempt
def send_model(request):
    context= {}
    if request.method == 'POST':
        key=request.POST.get('key')
        test_acc=request.POST.get('acc')
        test_loss=request.POST.get('loss')
        type=request.POST.get('type')
        modeltype=int(request.POST.get('modeltype'))
        modelfile=request.FILES.get('file')
        with  open(os.path.join(save_dir,key), 'wb') as f:
            for chunk in modelfile.chunks():
                f.write(chunk)
        ncl=Clients.objects.filter(Key=key).first()
        if ncl and test_loss:
            if float(test_loss)>0:
                ncl.Loss=test_loss
                ncl.save()
        keys=[cl.Key for cl in Clients.objects.filter(ModelType=modeltype,Status=1)]
        # print(len(keys))
        result=Util.check_fed_model(save_dir,keys,type,test_acc,test_loss,10)
        context['result']=result
        Util.setsession(key)
        print('send_model',context)
    return HttpResponse(json.dumps(context),content_type="application/json")
@csrf_exempt
def get_status(request):
    context= {}
    if request.method == 'POST':
        key=request.POST.get('key')
        type=request.POST.get('type')
        modeltype=int(request.POST.get('modeltype'))
        keys=[cl.Key for cl in Clients.objects.filter(ModelType=modeltype,Status=1)]
        context['modelurl']=''
        context['clientstatus']=Util.check_client(save_dir,key)
        context['result']=Util.check_client_all(save_dir,keys)
        print('context[\'result\']',context['result'])
        if int(context['clientstatus'])==0:
            if os.path.exists(os.path.join(save_dir,'%s_model'%(key))):
                os.rename(os.path.join(save_dir,'%s_model'%(key)),os.path.join(save_dir,'%s_modelb'%(key)))
                context['modelurl']=os.path.join(save_dir,'%s_modelb'%(key)).replace(BASE_DIR,'')
            # else:
            #     Util.check_fed_model(save_dir,keys,type,0,10)
        if int(context['result'])==3 and int(context['clientstatus'])==1:
            Util.check_fed_model(save_dir,keys,type,0,10)
        print(context)
        Util.setsession(key)
        # Util.addtasklog(ut.save_dir,'get_status',taskid,clientid,'result',context['result'],context['modelurl'],context['clienttrain'])
    return HttpResponse(json.dumps(context),content_type="application/json") 

@csrf_exempt
def changeStatus(request):
    context= {}
    if request.method == 'GET':
        key=request.GET.get('key')
        status=request.GET.get('status')
        context['result']=Util.setClientStatus(key,status)
    return HttpResponse(json.dumps(context),content_type="application/json") 

from django.http import FileResponse  
def download(request):
    context={}
    if request.method == 'GET':
        key=request.GET.get('key')
        client=Clients.objects.filter(Key=key).first()
        if client:
            file=open(os.path.join(save_dir,'%s_modelb'%(key)),'rb')
            response =FileResponse(file)
            response['Content-Type']='application/octet-stream'
            response['Content-Disposition']='attachment;filename="%s.model"'%(client.CName)
            return response
    return HttpResponse(json.dumps(context),content_type="application/json") 
 
@csrf_exempt
def deleteclient(request):
    context= {}
    if request.method == 'GET':
        key=request.GET.get('key')
        cl=Clients.objects.filter(Key=key).first()
        if cl:
            cl.delete()
            context['result']=1
    return HttpResponse(json.dumps(context),content_type="application/json") 