# Generated by Django 5.0.2 on 2024-04-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comingsoon', '0010_alter_mediashuttlecompetition_filter_variable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mediashuttlecompetition',
            name='training',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon')], default='1', max_length=20),
        ),
    ]