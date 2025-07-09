from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('<int:task_id>/toggle/', views.toggle_task, name='toggle_task'),
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
]