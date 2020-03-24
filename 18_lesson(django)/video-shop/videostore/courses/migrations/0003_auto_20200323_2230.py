# Generated by Django 3.0.4 on 2020-03-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='course_images', verbose_name='Изображение профиля'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Название URL'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название курса'),
        ),
    ]
