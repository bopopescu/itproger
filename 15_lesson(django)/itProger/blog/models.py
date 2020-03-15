from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .libs.slugify import slugify

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Article(models.Model):
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name='url'
    )

    def get_absolute_url(self):
        return reverse("new-detail", kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Artilce, self).save(*args, **kwargs)
