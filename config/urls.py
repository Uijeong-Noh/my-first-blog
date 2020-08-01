from django.contrib import admin
from django.urls import path, include
from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
