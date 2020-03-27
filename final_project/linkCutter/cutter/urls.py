from django.contrib import admin
from django.urls import path
from .views import home_page, about,  HrefCreateView
from users import views as userView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about, name='about'),
    path('hrefs/', HrefCreateView.as_view(), name='hrefs'),
    path('reg/', userView.register, name='reg'),
    path('profile/', userView.showprofile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/',
         authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'),
         name='pass-reset'),
]
