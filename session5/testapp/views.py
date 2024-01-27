from django.shortcuts import render

# Create your views here.
def page(request):
    count = request.session.get('count',0)
    count+=1
    request.session['count'] = count
    request.session.set_expiry(60)
    print("sachin",request.session.get_expiry_age())
    return render(request,'testapp/page.html',{'count':count})
