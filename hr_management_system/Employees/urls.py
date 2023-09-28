from django.urls import path
from Employees import views

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('show/<int:id>/', views.employee_show, name='employee-show'),
    path('edit/<int:id>/', views.employee_edit, name='employee-edit'),
    path('delete/<int:id>/', views.employee_delete, name='employee-delete'),
    
    path('attendance/', views.employee_attendance, name='employee_attendance'),
    path('designations/', views.employee_designations, name='employee_designations'),
    path('holidays/', views.employee_holidays, name='employee_holidays')
]