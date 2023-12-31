from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from Employees.models import EmployeeDetail
from Project.models import AssignProject
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.mail import send_mail
from django.db.utils import IntegrityError

class UsersView(View):
    def get(self, request):
        total_user= User.objects.count()
       
        context={
            'total_user': total_user,
        }
        
        return render(request, 'dashboard.html', context)
    

class DashboardView(View):
    def get(self, request):
        employee_count = EmployeeDetail.objects.count()

        context = {
            'employee_count': employee_count,
        }
        
        return render(request, 'dashboard.html', context)
    
class ProjectView(View):
    def get(self, request):
        project_count= AssignProject.objects.count()
    
        context = {
            'project_count': project_count,
        }
            
        return render(request, 'dashboard.html', context)
    

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
          
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Succesfully")
            return redirect('employee_list')
        
        else:
            messages.error(request, "Login fail..")
            return redirect('login')
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out succesfully")
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new user and handle password hashing
        try: 
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = f_name
            user.last_name = l_name
            user.is_active = True
            user.save()
            send_mail(
                'Account Registration',  # subject
                'Your account has been created succesfully', #message
                'thapajohn2057@gmail.com', #sender email address
                [user.email], #recipent address
            )
                
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('register')
