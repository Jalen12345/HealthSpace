from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.IntegerField(default=0)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Goals = models.CharField(max_length=255)
    New = models.BooleanField(default=True)
