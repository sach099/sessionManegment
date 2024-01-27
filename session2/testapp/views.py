from django.shortcuts import render
from testapp.forms import Login
# Create your views here.
def home(request):
    form = Login()
    return render(request,'testapp/home.html',{'form':form})

def first(request):
    name = request.GET['name']
    response = render(request,'testapp/first.html',{'name':name})
    response.set_cookie('name',name)
    return response

import datetime
def dt(request):
   name = request.COOKIES.get('name')
   date_time = datetime.datetime.now()
   return render(request,'testapp/result.html',{'date_time':date_time,'name':name})
