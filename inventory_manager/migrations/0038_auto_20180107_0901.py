# Generated by Django 2.0 on 2018-01-07 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0037_auto_20171231_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 1, 7, 9, 1, 48, 678803), verbose_name='Ημερομηνία'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Τιμή Μονάδας'),
        ),
    ]