from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('valor_total',)

admin.site.register(Pedido, PedidoAdmin)