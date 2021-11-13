from django.db import models


class Clients(models.Model):
    CID= models.AutoField(primary_key=True)
    ModelType=models.IntegerField(default=-1)
    CName=models.CharField(max_length=300)
    Key=models.CharField(max_length=300,default='')
    Loss=models.CharField(max_length=10,default='')
    Status=models.IntegerField(default=0)
    LoginStatus=models.IntegerField(default=0)