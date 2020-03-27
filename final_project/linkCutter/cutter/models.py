from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Имя пользователя")
    url = models.CharField(max_length=200, verbose_name=u'Full Href')
    url_name = models.CharField(max_length=50, verbose_name=u'Short url name', unique=True)

    def __str__(self):
        return f' URL {self.url_name} от пользователя {self.user.username}'

    def get_absolute_url(self):  # new
        return reverse('hrefs')
