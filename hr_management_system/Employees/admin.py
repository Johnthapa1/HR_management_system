from django.contrib import admin
from Employees.models import  EmployeeDetail, AttendanceRecord, EmployeeDesignation

# Register your models here.

class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ["employee_name", "employee_designation", "employee_contact", "employee_image"]
    search_fields = ["employee_name", "employee_designation", "employee_contact", "employee_image"]
    list_filter = ["employee_name",]

admin.site.register(EmployeeDetail,EmployeeDetailAdmin )
admin.site.register(AttendanceRecord)
admin.site.register(EmployeeDesignation)
