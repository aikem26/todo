from django.db import models
from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    creatted_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
