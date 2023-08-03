from django import forms
from Employees.models import EmployeeDetail, AttendanceRecord

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        # fields = ("__all__",) #for all attributes
        
        fields = ("employee_code", "employee_name","employee_designation", "employee_contact")
        model = EmployeeDetail
        
class AttendanceRecordCreateForm(forms.ModelForm):
    class Meta:
        fields = ("employee", "date")
        model = AttendanceRecord
        


