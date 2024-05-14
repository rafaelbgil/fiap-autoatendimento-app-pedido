from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    #api endpoints
    path('cliente/', views.ClienteView.as_view(), name="Lista clientes"),
    path('cliente/<str:uuid>/', views.ClienteDetalhesView.as_view()),
    path('auth/', views.AuthView.as_view()),
    path('criar_usuario/', views.CriarUsuarioView.as_view()),
    path('pedido/', views.PedidoView.as_view()),
    path('pedido/<str:id>/', views.PedidoDetalhesView.as_view()),
    path('pedido/<str:id>/atualizarStatus/', views.PedidoAtualizarStatusView.as_view()),
    path('pedido/mercadopago/<str:uuid>/', views.PedidoMercadopagoDetalhesView.as_view()),
    # Schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swager and redoc:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
