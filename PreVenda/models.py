from django.db import models

# Create your models here.
class Prevenda(models.Model):
    prevenda = models.CharField(max_length=300, primary_key=True)
    codigo = models.IntegerField()
    status = models.IntegerField('Status: 1 Aguardando / 8 Concluido')

    class Meta:
        db_table = 'prevendas'
