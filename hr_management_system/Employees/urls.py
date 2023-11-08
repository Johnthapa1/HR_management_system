from django.urls import path
from Employees import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('show/<int:pk>/', views.employee_show, name='employee_show'),
    path('edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    
    path('attendance/', views.employee_attendance, name='employee_attendance'),
    path('designations/', views.employee_designations, name='employee_designations'),
    path('holidays/', views.employee_holidays, name='employee_holidays'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 