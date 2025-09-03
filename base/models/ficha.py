from django.db import models

# Create your models here.
class ficha(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name',max_length=50)
    classe = models.CharField('class',max_length=50)
    antecedente = models.CharField('antecedente',max_length=50)
    player = models.CharField('player',max_length=50)
    raca = models.CharField('raça',max_length=50)
    alinhamento = models.CharField('alinhamento',max_length=50)
    personalidade = models.CharField('personalidade',max_length=10000)
    ideais = models.CharField('ideais',max_length=100)
    vinculos = models.CharField('vinculos',max_length=1000)
    fraquezas = models.CharField('fraquezas',max_length=100)
    talentos = models.CharField('talentos',max_length=1000)
    pc = models.IntegerField('')
    pp = models.IntegerField('')
    pe = models.IntegerField('')
    po = models.IntegerField('')
    pl = models.IntegerField('')
    equipamentos = models.CharField('equipamentos',max_length=1000)
    proficiencias_idiomas = models.CharField('idioma',max_length=1000)

    xp = models.IntegerField()
    proficiencia = models.IntegerField()
    inspiracao = models.CharField('foda',max_length=100)


    def __str__(self):
        return self.name