# Generated by Django 4.1.7 on 2023-02-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0006_alter_ratehotel_stars_alter_ratetourismplace_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='avg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
