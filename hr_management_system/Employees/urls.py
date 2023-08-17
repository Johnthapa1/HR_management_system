from django.urls import path
from Employees import views

urlpatterns = [
     path('all/', views.employee_all, name='employee_all'),
    path('attendance/', views.employee_attendance, name='employee_attendance'),
    path('designations/', views.employee_designations, name='employee_designations'),
    path('holidays/', views.employee_holidays, name='employee_holidays')
]