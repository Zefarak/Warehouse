# Generated by Django 2.0 on 2018-03-18 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0042_auto_20180318_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 14, 22, 46, 956681), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
