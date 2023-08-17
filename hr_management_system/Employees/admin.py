from django.contrib import admin
from Employees.models import  EmployeeDetail, AttendanceRecord, EmployeeDesignation

# Register your models here.
admin.site.register(EmployeeDetail)
admin.site.register(AttendanceRecord)
admin.site.register(EmployeeDesignation)
