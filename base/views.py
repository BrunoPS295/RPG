from django.shortcuts import render
from .models.item import item
from ficha.models.ficha import base


#Create your views here.

def index(request):
    fichas = base.objects.order_by('name')
    context = {'fichas': fichas}
    return render(request, 'base/index.html', context)

def items(request):
    items = item.objects.order_by('name')
    context = {'items': items}
    return render(request, 'base/items.html', context)