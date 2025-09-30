from django.shortcuts import render
from .models import base

#Create your views here.

def index(request):
    fichas = base.objects.order_by('name')
    context = {'fichas': fichas}
    return render(request, 'ficha/index.html', context)

