# Generated by Django 2.0 on 2018-06-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0004_auto_20180607_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='vacation_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vacation',
            name='days',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
