from django.contrib import admin
from django.urls import path, include
from myapp import urls
urlpatterns = [
    # Include the URLs for the Django admin interface
    path('admin/', admin.site.urls),
    
    # Include the URLs for your API views (assuming they are in 'myapp.urls')
    path('api/', include('myapp.urls')),
]
