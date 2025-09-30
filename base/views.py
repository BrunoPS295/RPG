from django.shortcuts import render
from .models import item



#Create your views here.

def index(request):
    return render(request, 'base/index.html')

def items(request):
    items = item.objects.order_by('name')
    context = {'items': items}
    return render(request, 'base/items.html', context)