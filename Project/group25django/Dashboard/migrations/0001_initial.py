# Generated by Django 3.1.1 on 2021-10-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Macros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DailyCalories', models.IntegerField(verbose_name="Today's Calories:")),
                ('Protein', models.IntegerField(verbose_name='grams')),
                ('Fat', models.IntegerField(verbose_name='grams')),
                ('Carbs', models.IntegerField(verbose_name='grams')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=75)),
                ('age', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('permission', models.BooleanField(default=False)),
            ],
        ),
    ]
