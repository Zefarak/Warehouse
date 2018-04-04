# Generated by Django 2.0 on 2017-12-16 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0003_auto_20171216_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='costumer_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.CostumerAccount', verbose_name='Πελάτης'),
        ),
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 4, 59, 684845), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
