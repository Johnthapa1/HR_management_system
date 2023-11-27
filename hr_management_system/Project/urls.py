from django.urls import path
from Project import views

urlpatterns = [
    path('projects/', views.add_project, name="add_project")
    
]
