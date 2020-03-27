from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Имя пользователя")
    email = models.CharField(default='user.email', max_length=200, verbose_name=u'Email')
    # img = models.ImageField(default='default.jpg', upload_to='user_images', verbose_name=u"Фото профиля")

    def __str__(self):
        return f' Профайл пользователя {self.user.username}'


    #
    # def save(self, **kwargs):
    #     super().save(**kwargs)
    #     mail = self.user.email
    #
    #     image = Image.open(self.img.path)
    #
    #     if image.height > 64 or image.width > 64:
    #         resize = (256, 256)
    #         image.thumbnail(resize)
    #         image.save(self.img.path)
