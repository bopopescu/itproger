# Generated by Django 3.0.4 on 2020-03-20 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20200320_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agree',
            field=models.BooleanField(default=True, verbose_name='Соглашение про отправку уведомлений на почту'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='user_images', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя'),
        ),
    ]
