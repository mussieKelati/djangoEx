"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import HomeQ
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from django.http.response import HttpResponse
from .import views




urlpatterns = [
   path('admin/', admin.site.urls),
    # path('my_app', include ('my_app.urls')),
    path('sec_app', include ('sec_app.urls')),
    path('chalenges/', include('third_app.urls')),
    path('exercise4/', include('exercise4.urls'))
]
