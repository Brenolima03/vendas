from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.FloatField()

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data = models.DateField()
    cliente = models.CharField(max_length=20)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')

    @property
    def valor_total(self):
        total_pedido = 0
        for item_pedido in self.itempedido_set.all():
            total_pedido += item_pedido.valor_total_item
        return round(total_pedido, 2)

    def __str__(self):
        return self.cliente

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    @property
    def valor_total_item(self):
        return self.produto.valor * self.quantidade