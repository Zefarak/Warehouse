# Generated by Django 2.0.2 on 2018-05-20 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0003_auto_20180514_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 5, 20, 14, 21, 24, 501524), verbose_name='Ημερομηνία'),
        ),
    ]
