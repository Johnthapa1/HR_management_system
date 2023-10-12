from django.shortcuts import render, redirect
from Employees.forms import EmployeeCreateForm, AttendanceRecordCreateForm, EmployeeDesignationCreateForm
from Employees.models import EmployeeDesignation, EmployeeDetail, AttendanceRecord
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# def employee_departments(request):
#     employee_department_create_form = EmployeeDepartmentCreateForm()
#     context = {"employeeDepartmentForm": employee_department_create_form, "title": "Employee Departments"}
#     return render(request, 'employees/employee_departments.html', context)
@login_required(login_url='/login/')
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
            messages.success(request, "Added succesfully")
            return redirect("employee_list")
        return redirect("employee_add")
         
    return render(request, 'employees/employee_add.html', context)

@login_required(login_url='/login/')
def employee_list(request):
    list_of_employee= EmployeeDetail.objects.all()
    context= {"data": list_of_employee }
    return render(request, 'employees/employee_list.html', context)

@login_required(login_url='/login/')
def employee_show(request, pk):
    employee_obj= EmployeeDetail.objects.get(pk=pk)
    context={"data": employee_obj}
    return render(request, 'employees/employee_show.html', context)

@login_required(login_url='/login/')
def employee_edit(request, pk):
    employee_obj=EmployeeDetail.objects.get(pk=pk)
    designation_obj=EmployeeDesignation.objects.all()
    context={"data": employee_obj, "employee_designation": designation_obj}
    
    if request.method == "POST":
        employee_obj= EmployeeCreateForm(data=request.POST, instance=employee_obj)
        if employee_obj.is_valid():
            employee_obj.save()
            messages.success(request, "Updated succesfully")
            return redirect("employee_show", pk)   #redirecting to url having pk or id
         
    return render(request, 'employees/employee_edit.html', context)

@login_required(login_url='/login/')
def employee_delete(request, pk):
    employee_obj= EmployeeDetail.objects.get(pk=pk)
    
    if request.method=='POST':
        employee_obj.delete()
        messages.success(request, "Deleted sucessfully")
        return redirect('employee_list')
    
    else:
        context = {"data": employee_obj}
        return render(request, 'employees/employee_delete.html', context)
@login_required(login_url='/login')
def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

@login_required(login_url='/login')
def employee_designations(request):
    employee_designation_create_form = EmployeeDesignationCreateForm()
    context = {"employeeDesignationForm":employee_designation_create_form, "title": "Employee Designation" }
    return render(request, 'employees/employee_designations.html', context)

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')

