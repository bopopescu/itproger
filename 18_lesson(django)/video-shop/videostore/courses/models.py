from django.db import models
from django.urls import reverse
from PIL import Image


class Course(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='course_images/')
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        super().save(**kwargs)

        image = Image.open(self.img.path)

        if image.height > 400 or image.width > 400:
            resize = (600, 600)
            image.thumbnail(resize)
            image.save(self.img.path)


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

