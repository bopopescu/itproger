from django.db import models
from django.contrib.auth.models import User
from .choises import GENDER_CHOICES
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Имя пользователя")
    img = models.ImageField(default='default.jpg', upload_to='user_images', verbose_name=u"Фото профиля")
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name=u"Пол")
    agree = models.BooleanField(default=True, verbose_name=u"Соглашение про отправку уведомлений на почту")

    def __str__(self):
        return f' Профайл пользователя {self.user.username}'

    def save(self, **kwargs):
        super().save(**kwargs)

        image = Image.open(self.img.path)

        if image.height > 64 or image.width > 64:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)
