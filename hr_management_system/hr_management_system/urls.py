from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('Employees.urls')),
    path('', include('Accounts.urls')),
    path('project/', include('Project.urls'))
]
