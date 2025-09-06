from django.contrib import admin
from ficha.models.base import *
from ficha.models.inventario import *
from ficha.models.info import *
from ficha.models.atributo import *
from ficha.models.ataque import *

# Register your models here.
admin.site.register(ataque)
admin.site.register(atributo)
admin.site.register(base)
admin.site.register(info)
admin.site.register(inventario)
