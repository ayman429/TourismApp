# Generated by Django 4.1.7 on 2023-02-24 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0007_hotel_avg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='avg',
        ),
    ]
