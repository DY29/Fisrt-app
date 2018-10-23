from django.shortcuts import render
from .models import Notice
def index(request):
    notice= Notice.objects.all()
    return render(request, 'firstapp/index.html',{'list':notice})

def detail(request):
    item=Notice.objects.get(id=1)
    return render(request, 'firstapp/detail.html',{'item':item})
