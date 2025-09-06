from django.db import models


# Create your models here.
class base(models.Model):
    name = models.CharField(null=True, blank=True,max_length=50)
    personalidade = models.CharField(null=True, blank=True,max_length=10000)
    ideais = models.CharField(null=True, blank=True,max_length=100)
    vinculos = models.CharField(null=True, blank=True,max_length=1000)
    fraquezas = models.CharField(null=True, blank=True,max_length=100)
    talentos = models.CharField(null=True, blank=True,max_length=1000)
    proficiencias_idiomas = models.CharField(null=True, blank=True,max_length=1000)

    def __str__(self):
        return str(self.name)