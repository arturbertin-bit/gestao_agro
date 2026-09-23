from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField()