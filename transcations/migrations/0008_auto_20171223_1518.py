# Generated by Django 2.0 on 2017-12-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0007_auto_20171223_1216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixedcostinvoice',
            options={'ordering': ['is_paid', '-date_expired'], 'verbose_name_plural': '3. Εντολές Πληρωμών'},
        ),
    ]