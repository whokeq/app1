from urllib import response
from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    context={
        'title':'home',
        'content':'главная cтраница магазина под названием ""',
    }
    return render(request,'main/index.html',context)

def about(request):
    return render(request,'main/about.html')
