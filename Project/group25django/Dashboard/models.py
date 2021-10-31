from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.CharField(max_length=75)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName


class Macro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    currentWeight = models.IntegerField("Weight (lb):", blank=True, null=True)
    calories = models.IntegerField("Calories:")
    protein = models.IntegerField("Protein (g):")
    fat = models.IntegerField("Total fat (g):")
    carbs = models.IntegerField("Total carbohydrates (g):")
