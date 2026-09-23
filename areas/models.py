from django.db import models

# Create your models here.
class Area(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.FloatField()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'areas'
        verbose_name = 'area'
        verbose_name_plural = 'areas'
        ordering = ['nome']
