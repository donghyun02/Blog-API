from django.db import models
# Create your models here.
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
