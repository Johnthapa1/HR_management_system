from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import auth

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username= request.POST.get('username')
        password= request.POST.get('password')
        # authenticating the user
        try:
            user= authenticate(request, username=username, password=password)
        except User.DoesNotExist as error:
            print(error)
            
        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            return redirect('login')
            

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        f_name= request.POST.get('first_name')
        l_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user= User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            user.first_name=f_name
            user.last_name=l_name
            user.is_active= True
            user.save()
            login(request, user)
            return redirect('login')
        return redirect('register')
