# Generated by Django 2.0 on 2017-12-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0002_auto_20171219_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixedcostinvoice',
            options={'verbose_name': '3. Εντολές Πληρωμών'},
        ),
        migrations.AlterModelOptions(
            name='fixedcosts',
            options={'verbose_name': '1. Κεντρική Κατηγορία Εξόδων   '},
        ),
        migrations.AlterModelOptions(
            name='fixedcostsitem',
            options={'verbose_name': '2. Λογαριασμοί και Πάγια έξοδα'},
        ),
        migrations.AlterModelOptions(
            name='occupation',
            options={'verbose_name_plural': '5. Απασχόληση'},
        ),
        migrations.AlterModelOptions(
            name='payroll',
            options={'verbose_name_plural': '4. Μισθοδοσία'},
        ),
        migrations.AlterModelOptions(
            name='payrollinvoice',
            options={'ordering': ['is_paid', 'date_expired'], 'verbose_name_plural': '7. Εντολές Πληρωμής Υπαλλήλων. '},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': '6. Υπάλληλος'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='hour_salary_sum',
        ),
        migrations.RemoveField(
            model_name='person',
            name='salary_paid',
        ),
        migrations.RemoveField(
            model_name='person',
            name='status',
        ),
        migrations.RemoveField(
            model_name='person',
            name='total_amount_paid',
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Υπόλοιπο'),
        ),
        migrations.AlterField(
            model_name='fixedcostinvoice',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Είναι πληρωμένο'),
        ),
        migrations.AlterField(
            model_name='fixedcostinvoice',
            name='payment_method',
            field=models.CharField(choices=[('1', 'Μετρητά'), ('2', 'Τραπεζική Κατάθεση'), ('3', 'Πιστωτική Κάρτα'), ('4', 'Paypal')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='payrollinvoice',
            name='payment_method',
            field=models.CharField(choices=[('1', 'Μετρητά'), ('2', 'Τραπεζική Κατάθεση'), ('3', 'Πιστωτική Κάρτα'), ('4', 'Paypal')], default='1', max_length=1),
        ),
    ]
