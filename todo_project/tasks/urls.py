# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),                     # GET for all tasks
    path('tasks/create/', views.TaskCreate.as_view(), name='task-create'),          # POST for creating a task
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),        # GET for single task by ID
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'), # DELETE for deleting a task by ID
    path('tasks/due-today/', views.TaskDueToday.as_view(), name='task-due-today'),  # GET for tasks due today
]
