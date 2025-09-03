from django.db import models
from ficha.models.base import base

class info(models.Model):
    name = models.ForeignKey(base, related_name="info", on_delete=models.CASCADE)
    classe = models.CharField(null=True, blank=True,max_length=50)
    antecedente = models.CharField(null=True, blank=True,max_length=50)
    player = models.CharField(null=True, blank=True,max_length=50)
    raca = models.CharField(null=True, blank=True,max_length=50)
    alinhamento = models.CharField(null=True, blank=True,max_length=50)
    xp = models.IntegerField(default='0')

    def __str__(self):
        return self.name