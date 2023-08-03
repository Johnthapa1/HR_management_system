from django.shortcuts import render
from Employees.forms import EmployeeCreateForm, AttendanceRecordCreateForm
# Create your views here.
def employee_all(request):
    employee_create_form = EmployeeCreateForm()  #creating form class object
    context = {"form": employee_create_form, "title": "Employee Details"}
    return render(request, 'employees/employee_all.html', context)

def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

def employee_departments(request):
    return render(request, 'employees/employee_departments.html')

def employee_designations(request):
    return render(request, 'employees/employee_designations.html')

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')