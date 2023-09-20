from django.shortcuts import render
from Employees.forms import EmployeeCreateForm, AttendanceRecordCreateForm, EmployeeDesignationCreateForm
from Employees.models import EmployeeDesignation, EmployeeDetail, AttendanceRecord
# Create your views here.
# def employee_departments(request):
#     employee_department_create_form = EmployeeDepartmentCreateForm()
#     context = {"employeeDepartmentForm": employee_department_create_form, "title": "Employee Departments"}
#     return render(request, 'employees/employee_departments.html', context)

def employee_all(request):
    employee_create_form = EmployeeCreateForm()  #creating form class object
    context = {"employeeDetailForm": employee_create_form, "title": "Add Employee"}
    
    if request.method == "POST":
        employee_code= request.POST.get('employee_code')
        employee_name= request.POST.get('employee_name')
        designation_obj = EmployeeDesignation.objects.get(id=request.POST.get('employee_designation'))
        employee_contact= request.POST.get('employee_contact')
        
        
        employee_all_obj = EmployeeDetail()
        employee_all_obj.employee_code = employee_code
        employee_all_obj.employee_name = employee_name
        employee_all_obj.employee_designation= designation_obj    # passing designation object (foreign key object)
        employee_all_obj.employee_contact = employee_contact
        employee_all_obj.save()
        
        
    return render(request, 'employees/employee_all.html', context)

def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

def employee_designations(request):
    employee_designation_create_form = EmployeeDesignationCreateForm()
    context = {"employeeDesignationForm":employee_designation_create_form, "title": "Employee Designation" }
    return render(request, 'employees/employee_designations.html', context)

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')

