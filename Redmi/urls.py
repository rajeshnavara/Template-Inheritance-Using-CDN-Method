"""Redmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Note9.views import *
from Note4.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/',Func1,name='Func1'),
    path('2/',Func2,name='Func2'),
    path('a/',parent,name='parent'),
    path('b/',child,name='child'),
]
