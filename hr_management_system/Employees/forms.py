from django import forms
from Employees.models import EmployeeDetail, AttendanceRecord, EmployeeDesignation

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        # fields = ("__all__",) #for all attributes
        
        fields = ("employee_code", "employee_name","employee_designation", "employee_contact", "employee_image")
        model = EmployeeDetail
        
class AttendanceRecordCreateForm(forms.ModelForm):
    class Meta:
        fields = ("employee", "date")
        model = AttendanceRecord
        
# class EmployeeDepartmentCreateForm(forms.ModelForm):
    
#     class Meta:
#         fields = ("department_name",)
#         model = EmployeeDepartment

class EmployeeDesignationCreateForm(forms.ModelForm):
    
    class Meta:
        fields= ("designation_name",)
        model = EmployeeDesignation
        

        


