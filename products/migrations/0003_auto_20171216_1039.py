# Generated by Django 2.0 on 2017-12-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171216_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='measure_unit',
            field=models.CharField(blank=True, choices=[('1', 'Τεμάχια'), ('2', 'Κιλά'), ('3', 'Διαθέσιμο με παραγγελία'), ('4', 'Προσωρινά μη διαθέσιμο')], max_length=1, null=True),
        ),
    ]
