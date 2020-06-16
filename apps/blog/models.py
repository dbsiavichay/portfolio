# Django
from django.db import models


class Media(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    file_extensionm = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=128)
    cover = models.ImageField(upload_to='posts')
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
