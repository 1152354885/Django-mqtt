import turtle
from django import http
from django.shortcuts import render
from sqlite3Exp.models import stuInfo
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
# Create your views here.
def addinfo(request):
    #myname=request.GET['UID']
     #myage=int(request.GET['age'])
     #stuInfo.objects.create(name=myname,age=myage)
     #stuInfo.objects.create(UID=myname)
     #a=stuInfo.objects.filter(age='12')
     #return JsonResponse(a)
    

    a=stuInfo.objects.order_by('-id')
    #print(a)
    for obj in a:      
                json_data = serializers.serialize('json', a) #把数据库的数据序列化成json格式
                json_data = json.loads(json_data) #解析json格式
                data = []#
                for i in range(len(json_data)):#遍历数据，把数据放到列表中
                    data.append(json_data[i]['fields']) # field:去掉不要的model和pk值
                    
                
                   
                return JsonResponse(data,safe=False)#返回数据
                    
                    
 
