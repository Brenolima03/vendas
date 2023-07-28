from django.db import models

class Pedido(models.Model):
    data = models.DateField()
    cliente = models.CharField(max_length=20)
    produtos = models.CharField(max_length=20)
    valor = models.FloatField()
    quantidade = models.IntegerField()
    
    @property
    def valor_total(self):
        if self.valor is not None and self.quantidade is not None:
            return self.valor * self.quantidade
        else:
            return 0
    
    def __str__(self):
        return self.cliente 