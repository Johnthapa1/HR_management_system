from rest_framework import serializers
from Employees.models import EmployeeDesignation, EmployeeDetail

class EmployeeDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDesignation
        fields = ["id", "designation_name"]
        
class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = ["employee_code", "employee_name","employee_designation", "employee_contact"]