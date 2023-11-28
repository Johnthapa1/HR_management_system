from django.urls import path
from Project import views

urlpatterns = [
    path('add/', views.add_project, name="add_project"),
    path('list/', views.list_project, name="list_project")
    
]
