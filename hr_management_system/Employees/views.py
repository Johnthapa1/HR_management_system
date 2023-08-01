from django.shortcuts import render

# Create your views here.
def employee_all(request):
    return render(request, 'employees/employee_all.html')

def employee_attendance(request):
    return render(request,'employees/employee_attendance.html')

def employee_departments(request):
    return render(request, 'employees/employee_departments.html')

def employee_designations(request):
    return render(request, 'employees/employee_designations.html')

def employee_holidays(request):
    return render(request, 'employees/employee_holidays.html')