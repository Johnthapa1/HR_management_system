from django.contrib import admin
from Employees.models import  EmployeeDetail, AttendanceRecord, EmployeeDesignation

# Register your models here.

class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ["employee_name", "employee_designation", "employee_contact", "employee_image"]
    search_fields = ["employee_name", "employee_designation"]
    list_filter = ["employee_name", "employee_designation"] 

admin.site.register(EmployeeDetail, EmployeeDetailAdmin )
admin.site.register(AttendanceRecord)
admin.site.register(EmployeeDesignation)

#customizing admin panel title and headings
admin.site.site_title = "Admin Panel"  #page subtitle
admin.site.site_header = "HR Mangement System"   #page header
admin.site.index_title = "HRMS"  #page title
