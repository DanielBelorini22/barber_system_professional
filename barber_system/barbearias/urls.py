from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('barbearia/listar/', listar_barbearia, name="listar_barbearia"),
    path('barbearia/perfil/<int:pk>/', perfil_barbearia, name="perfil_barbearia"),
]
