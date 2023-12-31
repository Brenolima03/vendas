from django.urls import path, include
from rest_framework import routers
from .views import PedidoViewSet

router = routers.DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
