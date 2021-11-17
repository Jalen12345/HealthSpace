from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Macro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="macro", null=True)
    date = models.DateField(blank=True, null=True)
    currentWeight = models.IntegerField("Weight (lb):", blank=True, null=True)
    calories = models.IntegerField("Calories:")
    protein = models.IntegerField("Protein (g):")
    fat = models.IntegerField("Total fat (g):")
    carbs = models.IntegerField("Total carbohydrates (g):")

class index(models.Model):
    height = models.IntegerField("Height")
    weight = models.IntegerField("Weight")
class Sleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Sleep", null=True)
    date = models.DateField(blank=True, null=True)
    sleepHours = models.IntegerField("Hours of Sleep:", blank=True, null=True)
    wakeUp = models.TimeField(auto_now=False, auto_now_add=False)
    QUALITY_CHOICES = [
        ('G', 'Good'),
        ('F', 'Fair'),
        ('P', 'Poor'),
    ]
    quality = models.CharField(max_length=1, choices=QUALITY_CHOICES, default='F')
    
