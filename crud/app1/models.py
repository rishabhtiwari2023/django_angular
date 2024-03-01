from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.CharField(max_length=150)

class User1(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
   