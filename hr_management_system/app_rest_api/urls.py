from django.urls import path
from app_rest_api.views import EmployeeDesignationApiView, EmployeeDetailApiView

urlpatterns = [
    path('designation/', EmployeeDesignationApiView.as_view()),
    path('detail/', EmployeeDetailApiView.as_view())
    
]