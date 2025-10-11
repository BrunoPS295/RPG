from django.shortcuts import render
from .models.item import item
from .models.ficha import ficha


#Create your views here.

def index(request):
    fichas = ficha.objects.order_by('name')
    context = {'fichas': fichas}
    return render(request, 'base/index.html', context)

def ficha_detail(request):
    return render(request, 'base/ficha.html')

def items(request):
    items = item.objects.order_by('name')
    context = {'items': items}
    return render(request, 'base/items.html', context)