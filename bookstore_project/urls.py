

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    # User management
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('books', include('books.urls'))
]
