# Generated by Django 2.0 on 2017-12-16 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0002_auto_20171215_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 12, 16, 10, 37, 18, 650156)),
        ),
    ]
