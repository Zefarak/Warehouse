# Generated by Django 2.0 on 2017-12-27 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0032_auto_20171224_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 12, 27, 7, 52, 33, 795302), verbose_name='Ημερομηνία'),
        ),
    ]
