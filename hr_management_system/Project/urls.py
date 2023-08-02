from django.urls import path
from Project import views

urlpatterns = [
    path('projects/', views.projects, name="project_projects"),
    path('taskboard/', views.taskboard, name="project_taskbaord"),
    path('tasks/', views.tasks, name="project_tasks")
]
