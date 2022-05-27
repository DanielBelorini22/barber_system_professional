from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('cortes/', views.cortes, name='cortes'),
    path('cortes/novo/', views.novo_corte, name='cortes-novo'),
    path('cortes/editar/<int:pk>/', views.editar_corte, name='cortes-editar'),
    path('cortes/remover/<int:pk>/', views.remover_corte, name='cortes-remover'),
    path('tipo-cortes/', views.tipo_cortes, name='tipo-cortes'),
    path('tipo-cortes/novo/', views.novo_tipo_corte, name='tipo-cortes-novo'),
    path('tipo-cortes/editar/<int:pk>/', views.editar_tipo_corte, name='tipo-cortes-editar'),
    path('tipo-cortes/remover/<int:pk>/', views.remover_tipo_corte, name='tipo-cortes-remover'),
    path('dashboard/', views.dash_board, name='dashboard'),
    path('task/<int:pk>/', views.task_view, name='task-view'),
    path('newtask/', views.new_task, name='new-task'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
    path('changestatus/<int:pk>/', views.change_status, name='change-status'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]
