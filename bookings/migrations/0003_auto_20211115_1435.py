# Generated by Django 3.2.7 on 2021-11-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20211015_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='file_link',
            field=models.CharField(default='dummy link', max_length=200),
            preserve_default=False,
        ),
    ]