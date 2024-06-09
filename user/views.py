from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Notice 

def all_notices(request):
    all_notices = Notice.objects.all()
    if request.method=="GET":
        notice=request.GET.get('query')
        if notice!=None:
            all_notices = Notice.objects.filter(subject__icontains=notice)
            
    context = {'result':all_notices}
    return render(request, 'user/noticehub.html/',context)
    
def home(request):
    context = {}
    return render(request, 'user/home.html',context)

def about(request):
    context = {}
    return render(request, 'user/about.html',context)

def contact(request):
    context = {}
    return render(request, 'user/contact.html',context)

def news(request):
    context = {}
    return render(request, 'user/news.html',context)

def our_team(request):
    context = {}
    return render(request, 'user/our_team.html',context)

def service(request):
    context = {}
    return render(request, 'user/service.html',context)

