from django.db import models
from ficha.models.base import base

class atributos(models.Model):
    name = models.ForeignKey(base, related_name="atributos", on_delete=models.CASCADE)
    proficiencia = models.IntegerField(default='0')
    inspiracao = models.CharField(null=True, blank=True,max_length=100)

    def __str__(self):
        return self.name