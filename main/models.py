from django.db import models
from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    creatted_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateField()
    is_favorite = models.BooleanField(default=False)


    
