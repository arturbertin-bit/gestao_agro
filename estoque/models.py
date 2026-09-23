from django.db import models

from produtos.models import Produto


# Create your models here.
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()