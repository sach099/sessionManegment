from django.shortcuts import render
from testapp.forms import Name,Age,Gf
# Create your views here.
def home(request):
    form = Name()
    return render(request,'testapp/name.html',{'form':form})

def ag(request):
    name = request.GET['username']
    form = Age()
    request.session['username']=name
    return render(request,'testapp/age.html',{'form':form,'name':name})

def gfname(request):
    age = request.GET['userage']
    form = Gf()
    request.session['userage']=age
    name = request.session['username']
    return render(request,'testapp/gf.html',{'form':form,'name':name})

def result(request):
    gf_name = request.GET['gf_name']
    request.session['gf_name'] = gf_name
    name = request.session['username']
    age = request.session['userage']
    return render (request,'testapp/result.html')