from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('cookbook/', include('cookbook.urls')), 
    path('__debug__/', include('debug_toolbar.urls')),
]
