# Generated by Django 5.0.2 on 2024-04-04 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comingsoon', '0006_mediashuttletraining_number_of_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediashuttletraining',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
