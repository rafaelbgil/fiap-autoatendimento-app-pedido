from django.contrib import admin

# Register your models here.
from api.models import Cliente, Pedido, ItemPedido, Cobranca

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Cobranca)