from django.shortcuts import render
from testapp.forms import Name,Age,Gf
# Create your views here.

def name(request):
    form = Name()
    return render(request,'testapp/name.html',{'form':form})
  

def age(request):
    name = request.GET['name']
    form = Age()
    response= render(request,'testapp/age.html',{'form':form,'name':name})
    response.set_cookie('name',name)
    return response

def gf(request):
    userage = request.GET['age']
    form = Gf()
    name = request.COOKIES.get('name')
    response= render(request,'testapp/gf.html',{'form':form,'name':name})
    response.set_cookie('age',userage)
    return response

def result(request):
    g_f = request.GET['gf_name']
    name = request.COOKIES.get('name')
    userage = request.COOKIES.get('age')
    response= render(request,'testapp/result.html',{'name':name,'age':userage,'g_f':g_f})
    response.set_cookie('g_f',g_f)
    return response

