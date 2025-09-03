from django.contrib import admin
from ficha.models.base import *
from ficha.models.inventario import *
from ficha.models.info import *
from ficha.models.atributos import *
from ficha.models.ataques import *

# Register your models here.
admin.site.register(ataque)
admin.site.register(atributos)
admin.site.register(base)
admin.site.register(info)
admin.site.register(inventario)
