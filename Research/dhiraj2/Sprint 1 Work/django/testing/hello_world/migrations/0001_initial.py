# Generated by Django 3.2.7 on 2021-10-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Goals', models.CharField(max_length=255)),
                ('New', models.BooleanField(default=True)),
            ],
        ),
    ]