from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('task/<int:pk>/', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:pk>/', views.editTask, name='edit-task'),
    path('changestatus/<int:pk>/', views.changeStatus, name='change-status'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task'),
]
