from django.urls import path
from Accounts import views

urlpatterns = [
    path('accounts/login', views.login.html, name="account_login"),
    path('accounts/register', views.reister.html, name="account_register"),
    path('accounts/profile', views.profile.html, name="account_profile")
]
