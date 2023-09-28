from django.shortcuts import render, redirect
from Employees.forms import EmployeeCreateForm, AttendanceRecordCreateForm, EmployeeDesignationCreateForm
from Employees.models import EmployeeDesignation, EmployeeDetail, AttendanceRecord
# Create your views here.
# def employee_departments(request):
#     employee_department_create_form = EmployeeDepartmentCreateForm()
#     context = {"employeeDepartmentForm": employee_department_create_form, "title": "Employee Departments"}
#     return render(request, 'employees/employee_departments.html', context)

def employee_add(request):
    employee_create_form = EmployeeCreateForm()  #creating form class object
    context = {"employeeDetailForm": employee_create_form, "title": "Add Employee"}
    
    if request.method == "POST":
        employee_code= request.POST.get('employee_code')
        employee_name= request.POST.get('employee_name')
        designation_obj = EmployeeDesignation.objects.get(id=request.POST.get('employee_designation'))
        employee_contact= request.POST.get('employee_contact')
        
        #method 1
        
        # employee_add_obj = EmployeeDetail()
        # employee_add_obj.employee_code = employee_code
        # employee_add_obj.employee_name = employee_name
        # employee_add_obj.employee_designation= designation_obj    # passing designation object (foreign key object)
        # employee_add_obj.employee_contact = employee_contact
        # employee_add_obj.save()
        
        #method 2- storing data with form class object
        employee_add=EmployeeCreateForm(request.POST)
        if employee_add.is_valid():
            employee_add.employee_designation=designation_obj
            employee_add.save()
            return redirect("employee_list")
        return redirect("employee_add")
         
    return render(request, 'employees/employee_add.html', context)

def employee_list(request):
    list_of_employee= EmployeeDetail.objects.all()
    context= {"data": list_of_employee }
    return render(request, 'employees/employee_list.html', context)

# def employee_show(request, id):
#     return render(request, 'employees/employee_show.html')
def employee_show(request, id):
    employee = get_object_or_404(EmployeeDetail, id=id)
    return render(request, 'employees/employee_show.html', {'employee': employee})

def employee_edit(request, id):
    return render(request, 'employees/employee_edit.html')

def employee_delete(request, id):
    return redirect(request, 'employee_list')

def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

def employee_designations(request):
    employee_designation_create_form = EmployeeDesignationCreateForm()
    context = {"employeeDesignationForm":employee_designation_create_form, "title": "Employee Designation" }
    return render(request, 'employees/employee_designations.html', context)

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')

