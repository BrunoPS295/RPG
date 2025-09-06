from django.shortcuts import render
from .models import item

# Create your views here.
def index(request):
    return render(request, 'base/index.html', {'item': item})