from django.contrib import admin
from django.urls import path, include

from cases import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cases/',include('cases.urls')),
]