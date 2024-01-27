from django.shortcuts import render
from testapp.forms import Additems
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')


def add(request):
    form = Additems()
    response = render(request,'testapp/add.html',{'form':form})
    if request.method =='POST':
        form = Additems(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response
        
def display(request):
    return render(request,'testapp/display.html')