from django.contrib import admin
from django.urls import path
from Employees import views as employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', employee_views.employee_all, name='employee_all'),
    path('employees/attendance/', employee_views.employee_attendance, name='employee_attendance'),
    path('employees/departments/', employee_views.employee_departments, name='employee_departments'),
    path('employees/designations/', employee_views.employee_designations, name='employee_designations'),
    path('employees/holidays/', employee_views.employee_holidays, name='employee_holidays')
]
