from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Forum, name="forum-main"),
]
