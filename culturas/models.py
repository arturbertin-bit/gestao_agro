from django.db import models

from areas.models import Area
# Create your models here.
class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    data_plantio = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'
        ordering = ['nome']
