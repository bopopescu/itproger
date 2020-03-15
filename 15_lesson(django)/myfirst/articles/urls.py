from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="articles-index"),
    path("test/", views.test, name="articles-test")
]
