# Generated by Django 2.0 on 2017-12-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='margin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='store',
            name='markup',
            field=models.IntegerField(default=0),
        ),
    ]
