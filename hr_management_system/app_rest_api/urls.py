from django.urls import path
from app_rest_api.views import EmployeeDesignationApiView, EmployeeDetailApiView, EmployeeDesignationApiPkView, EmployeeDetailApiPKView

urlpatterns = [
    path('designation/', EmployeeDesignationApiView.as_view()),
    path('designation/<int:pk>/', EmployeeDesignationApiPkView.as_view()),
    path('detail/', EmployeeDetailApiView.as_view()),
    path('detail/<int:pk>/', EmployeeDetailApiPKView.as_view())
    
]