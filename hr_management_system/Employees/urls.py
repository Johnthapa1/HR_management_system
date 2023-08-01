from django.urls import path
from Employees import views

urlpatterns = [
     path('employees/', views.employee_all, name='employee_all'),
    path('employees/attendance/', views.employee_attendance, name='employee_attendance'),
    path('employees/departments/', views.employee_departments, name='employee_departments'),
    path('employees/designations/', views.employee_designations, name='employee_designations'),
    path('employees/holidays/', views.employee_holidays, name='employee_holidays')
]