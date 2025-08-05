from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('criar/', views.task_create, name = 'task_create'),
    path('editar/<int:pk>/', views.task_update, name = 'task_update'),
    path('deletar/<int:pk>/', views.task_delete, name = 'task_delete'),
    path('detalhes/<int:pk>/', views.task_detail, name = 'task_detail'),
]
