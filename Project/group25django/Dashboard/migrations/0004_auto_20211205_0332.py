# Generated by Django 3.2.9 on 2021-12-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_auto_20211205_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='carbs',
            field=models.IntegerField(verbose_name='Carbs(g):'),
        ),
        migrations.AlterField(
            model_name='index',
            name='fat',
            field=models.IntegerField(verbose_name='Fat(g):'),
        ),
        migrations.AlterField(
            model_name='index',
            name='height',
            field=models.IntegerField(verbose_name='Height(cm)'),
        ),
        migrations.AlterField(
            model_name='index',
            name='protein',
            field=models.IntegerField(verbose_name='Protein(g):'),
        ),
        migrations.AlterField(
            model_name='index',
            name='weight',
            field=models.IntegerField(verbose_name='Weight(Ib)'),
        ),
    ]