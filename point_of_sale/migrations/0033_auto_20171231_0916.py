# Generated by Django 2.0 on 2017-12-31 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0032_auto_20171231_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 9, 16, 33, 986877), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]