# Generated by Django 5.0.2 on 2024-04-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comingsoon', '0009_mediashuttlecompetition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediashuttlecompetition',
            name='filter_variable',
            field=models.CharField(default='departure', max_length=50),
        ),
        migrations.AlterField(
            model_name='mediashuttlecompetition',
            name='training',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='mediashuttletraining',
            name='filter_variable',
            field=models.CharField(default='departure', max_length=50),
        ),
    ]