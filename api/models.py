from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    profile = models.CharField(max_length=200)
