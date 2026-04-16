from urllib import response
from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    context={
        'title':'Нome - главная',
        'content':"Магазин мебели HOME",
    }
    return render(request,'main/index.html',context)

def about(request):
    context={
        'title':'Нome - О нас',
        'content':"О нас",
        'text_on_page':'текст какой крутой этот магазин'
    }
    return render(request,'main/about.html', context)
def contact(request):
    context={
        'title':'Нome - Контакты',
        'content':"Контактная информация",
        'text_on_page':'8 800 555 35 35'
    }
    return render(request,'main/about.html', context)

def delivery(request):
    context={
        'title':'Нome - Доставка и оплата',
        'content':"Условия доставки и оплаты",
        'text_on_page':'текст условия я не придумала'
    }
    return render(request,'main/about.html', context)
