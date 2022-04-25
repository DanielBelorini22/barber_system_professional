from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('barbearia/listar/', listar_barbearia, name="listar_barbearia"),
    path('barbearia/contato/', contato_barber_system, name="contato_barber_system"),
    path('barbearia/perfil/<int:pk>/', perfil_barbearia, name="perfil_barbearia"),
]
