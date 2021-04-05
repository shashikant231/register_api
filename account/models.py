from django.db import models


# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
