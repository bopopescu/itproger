from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.yourApp, name="yourApp-main"),
    path("example/test/Some", views.some, name="yourApp-some"),
]
