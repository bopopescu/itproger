from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='simpy-home'),
    path('uslugi/', views.uslugi, name='simpy-uslugi'),
    path('contacts/', views.contacts, name='simpy-contacts'),
    path('about/', views.about, name='simpy-about')
]
