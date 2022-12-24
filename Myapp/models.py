from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    tag = models.CharField(max_length=150)
    image = models.ImageField(upload_to="media", default="")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title



