# Generated by Django 2.0 on 2017-12-24 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0030_auto_20171223_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 12, 24, 9, 22, 55, 385761), verbose_name='Ημερομηνία'),
        ),
    ]