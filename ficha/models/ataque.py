from django.db import models
from ficha.models.base import base

class ataque(models.Model):
    name = models.ForeignKey(base, related_name="ataques", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)