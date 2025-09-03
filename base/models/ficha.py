from django.db import models

# Create your models here.
class ficha(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True,max_length=50)
    classe = models.CharField(null=True, blank=True,max_length=50)
    antecedente = models.CharField(null=True, blank=True,max_length=50)
    player = models.CharField(null=True, blank=True,max_length=50)
    raca = models.CharField(null=True, blank=True,max_length=50)
    alinhamento = models.CharField(null=True, blank=True,max_length=50)
    personalidade = models.CharField(null=True, blank=True,max_length=10000)
    ideais = models.CharField(null=True, blank=True,max_length=100)
    vinculos = models.CharField(null=True, blank=True,max_length=1000)
    fraquezas = models.CharField(null=True, blank=True,max_length=100)
    talentos = models.CharField(null=True, blank=True,max_length=1000)
    pc = models.IntegerField(default='0')
    pp = models.IntegerField(default='0')
    pe = models.IntegerField(default='0')
    po = models.IntegerField(default='0')
    pl = models.IntegerField(default='0')
    equipamentos = models.CharField(null=True, blank=True,max_length=1000)
    proficiencias_idiomas = models.CharField(null=True, blank=True,max_length=1000)

    xp = models.IntegerField(default='0')
    proficiencia = models.IntegerField(default='0')
    inspiracao = models.CharField(null=True, blank=True,max_length=100)


    def __str__(self):
        return self.name