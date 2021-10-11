# Generated by Django 3.2.7 on 2021-10-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
