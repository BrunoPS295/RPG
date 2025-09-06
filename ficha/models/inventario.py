from django.db import models
from ficha.models.base import base
from base.models import item

class inventario(models.Model):
    name = models.ForeignKey(base, related_name="inventario", on_delete=models.CASCADE)
    
    pc = models.IntegerField(default='0')
    pp = models.IntegerField(default='0')
    pe = models.IntegerField(default='0')
    po = models.IntegerField(default='0')
    pl = models.IntegerField(default='0')
    equipamento = models.ForeignKey(item, related_name="inventario", on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name