# Generated by Django 2.0 on 2017-12-22 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0020_auto_20171222_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 16, 1, 2, 459827), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]