from django.contrib import admin
from .models import Produto, Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data', 'valor_total')
    readonly_fields = ('valor_total',)
    inlines = [ItemPedidoInline]

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    pass
