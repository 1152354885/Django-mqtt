from operator import mod
from plistlib import UID
from stat import ST_UID
from time import time
from unicodedata import name
from django.db import models

# Create your models here.
class stuInfo(models.Model):
    id=models.AutoField(primary_key=True)
    Temp=models.CharField(max_length=10)
    time=models.CharField(blank=True,null=True,max_length=10)
class  hobby(models.Model):
    id=models.AutoField(primary_key=True)    
    Humi=models.CharField(max_length=50)
    time=models.CharField(blank=True,null=True,max_length=10)
    #stuid=models.ForeignKey(stuInfo,on_delete=models.CASCADE)
    
