from django.shortcuts import render

# Create your views here.
def catalog(request):
    context={
        'title':'Нome - каталог',
        'content':"Каталог магазина мебели HOME",
    }
    return render(request,'goods/catalog.html',context)

def product(request):
    context={
        'title':'Нome - каталог',
        'content':"Каталог магазина мебели HOME",
    }
    return render(request,'goods/product.html',context)

