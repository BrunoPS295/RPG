from django.db import models
from ficha.models.base import base

class ficha(models.Model):
    name = models.ForeignKey(base, related_name="ficha", on_delete=models.CASCADE)