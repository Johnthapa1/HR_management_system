from django.shortcuts import render
from Employees.forms import EmployeeCreateForm, AttendanceRecordCreateForm, EmployeeDesignationCreateForm
# Create your views here.
# def employee_departments(request):
#     employee_department_create_form = EmployeeDepartmentCreateForm()
#     context = {"employeeDepartmentForm": employee_department_create_form, "title": "Employee Departments"}
#     return render(request, 'employees/employee_departments.html', context)

def employee_all(request):
    employee_create_form = EmployeeCreateForm()  #creating form class object
    context = {"employeeDetailForm": employee_create_form, "title": "Employee Details"}
    return render(request, 'employees/employee_all.html', context)

def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

def employee_designations(request):
    employee_designation_create_form = EmployeeDesignationCreateForm()
    context = {"employeeDesignationForm":employee_designation_create_form, "title": "Employee Designation" }
    return render(request, 'employees/employee_designations.html', context)

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')

