from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('cortes/', views.tipo_cortes, name='tipo-cortes'),
    path('cortes/novo/', views.novo_tipo_cortes, name='tipo-cortes-novo'),
    path('dashboard/', views.dash_board, name='dashboard'),
    path('task/<int:pk>/', views.task_view, name='task-view'),
    path('newtask/', views.new_task, name='new-task'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
    path('changestatus/<int:pk>/', views.change_status, name='change-status'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]
