from django.contrib import admin
from django.urls import path
from Url_App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:key>', views.home_url, name='home_url')
]