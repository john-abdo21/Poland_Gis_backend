"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.front, name="front"),
    
    re_path(r'^api/complexSearch', views.complex_Search, name = 'complexSearch'),
    re_path(r'^api/requestData', views.all_Search, name = 'all_Search'),
    re_path(r'^api/requestPoint', views.point_Search, name = 'point_Search'),
]
