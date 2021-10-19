from django.db import models

from django.db.models.fields import DecimalField as d



# Create your models here.



class User(models.Model):

    first_name = models.CharField(max_length = 40)

    last_name = models.CharField(max_length = 40)

    email = models.CharField(max_length = 75)

    age = models.IntegerField()

    username = models.CharField(max_length = 30)

    permission = models.BooleanField(default = False)



    def __str__(self):

        return self.first_name



class ExcerciseDay(models.Model):

    WorkoutChoices = ["Push Day (Shoulders, Triceps, Biceps)", "Pull Day (Biceps, Back)", "Leg Day (Quads, Hamstrings Calves)"]

    UserWorkoutChoice = models.CharField(max_length = 1, choices=WorkoutChoices)





class Macros(models.Model):

    DailyCalories = models.IntegerField("Today's Calories:")

    Protein = models.IntegerField("grams")

    Fat = models.IntegerField("grams")

    Carbs = models.IntegerField("grams")



class DailyLimit(models.Model):

    CaloriesAttained = models.OneToOneField(

        Macros,

        on_delete = models.CASCADE,

        primary_key = False,

    )



    ProteinAttained = models.OneToOneField(

        Macros,

        on_delete = models.CASCADE,

        primary_key = False,

    )



    CarbsAttained = models.OneToOneField(

        Macros,

        on_delete = models.CASCADE,

        primary_key = False,

    )



    FatsAttained = models.OneToOneField(

        Macros,

        on_delete = models.CASCADE,

        primary_key = False,

    )



class HeightWeight(models.Model):

    WeightType = ["Pounds", "Kilograms"]

    HeightType = ["Feet & Inches", "Centimeters"]



    WeightTrackingType = d.CharField(max_length = 1, choices = WeightType)

    HeightTrackingType = d.CharField(max_length = 1, choices = HeightType)

    CurrentWeight = d.DecimalField()

    CurrentHeight = d.DecimalField()

    StartingWeight = d.DecimalField()

    StartingHeight = d.DecimalField()

    BMI = d.DecimalField()

