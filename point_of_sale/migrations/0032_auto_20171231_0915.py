# Generated by Django 2.0 on 2017-12-31 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0031_auto_20171228_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 9, 15, 31, 15264), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]