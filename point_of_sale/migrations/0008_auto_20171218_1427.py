# Generated by Django 2.0 on 2017-12-18 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0007_auto_20171218_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 14, 27, 40, 836600), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]