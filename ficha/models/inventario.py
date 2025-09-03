from django.db import models
from ficha.models.base import base

class inventario(models.Model):
    name = models.ForeignKey(base, related_name="inventario", on_delete=models.CASCADE)
    pc = models.IntegerField(default='0')
    pp = models.IntegerField(default='0')
    pe = models.IntegerField(default='0')
    po = models.IntegerField(default='0')
    pl = models.IntegerField(default='0')
    equipamentos = models.CharField(null=True, blank=True,max_length=1000)

    def __str__(self):
        return self.name