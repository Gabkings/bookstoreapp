

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    
]
