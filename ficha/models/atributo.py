from django.db import models
from ficha.models.base import base

class atributo(models.Model):
    name = models.ForeignKey(base, related_name="atributo", on_delete=models.CASCADE)
    
    proficiencia = models.IntegerField(default='0')
    inspiracao = models.CharField(null=True, blank=True,max_length=100)

    def __str__(self):
        return self.name