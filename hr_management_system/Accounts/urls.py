from django.urls import path
from Accounts import views

urlpatterns = [
    path('login/', views.login, name="account_login"),
    path('register/', views.register, name="account_register"),
    path('profile/', views.profile, name="account_profile")
]