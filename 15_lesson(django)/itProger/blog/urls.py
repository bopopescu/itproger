from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contacts/', views.contacts, name='blog-contacts'),
    path('practice/', views.practice, name='blog-practice'),
    path("practice/lessons", views.lessons,name='practice-lessons'),
    path('practice/about', views.about, name='practice-about'),
    path('news/<slug:slug>.html',views.NewDetailView.as_view(), name='news-detail')
]
