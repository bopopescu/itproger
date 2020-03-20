from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userView
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('reg/', userView.register, name='reg'),
    path('profile/', userView.showprofile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'),name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'),name='exit')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
