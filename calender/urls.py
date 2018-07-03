"""calenderproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('login',auth_views.login,name='login'),
    path('calender',views.calender,name='calender'),
    path('logout',auth_views.logout,{'next_page': '/'},name='logout'),
    path('entry/<int:pk>',views.details,name='details'),
    path('entry/add',views.add,name='add'),
    path('entry/delete/<int:pk>',views.delete,name='delete'),

]
