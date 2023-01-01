"""Ohioshoes URL Configuration

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
from django.conf import settings

from pages.views import homepage_view, about_view, base_view, contact_view, help_view
from history.views import history_form_view

urlpatterns = [
    path('', base_view),
    path('home/', homepage_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('help/', help_view),
    path('buy/', history_form_view),
    path('admin/', admin.site.urls),

]
