# Generated by Django 2.0 on 2017-12-23 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0025_auto_20171223_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='retailorder',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 23, 15, 18, 57, 150178), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
