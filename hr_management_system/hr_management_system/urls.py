from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('Employees.urls')),
    path('', include('Accounts.urls')),
    path('project/', include('Project.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('app_rest_api.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
    
