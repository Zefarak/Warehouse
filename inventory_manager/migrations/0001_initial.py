# Generated by Django 2.0 on 2018-05-14 09:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
import inventory_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_created', models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 5, 14, 12, 34, 19, 875698), verbose_name='Ημερομηνία')),
                ('code', models.CharField(max_length=40, verbose_name='Αριθμός Παραστατικού')),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='')),
                ('total_price_no_discount', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Αξία προ έκπτωσης')),
                ('total_discount', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Αξία έκπτωσης')),
                ('total_price_after_discount', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Αξία μετά την έκπτωση')),
                ('total_taxes', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Φ.Π.Α')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Τελική Αξία')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Πληρωμένο Ποσό')),
                ('taxes_modifier', models.CharField(choices=[('1', '13'), ('2', '23'), ('3', '24'), ('4', '0')], default='3', max_length=1)),
                ('is_paid', models.BooleanField(default=False, verbose_name='Πληρώθηκε')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name_plural': '1. Τιμολόγια',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('1', 'Τεμάχια'), ('2', 'Κιλά'), ('3', 'Κιβώτια')], default='1', max_length=1)),
                ('discount', models.IntegerField(default=0, verbose_name='Εκπτωση %')),
                ('taxes', models.CharField(choices=[('1', '13'), ('2', '23'), ('3', '24'), ('4', '0')], default='3', max_length=1)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ποσότητα')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Τιμή Μονάδας')),
                ('total_clean_value', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Συνολική Αξία χωρίς Φόρους')),
                ('total_value_with_taxes', models.DecimalField(decimal_places=2, default=0, max_digits=14, verbose_name='Συνολική Αξία με φόρους')),
                ('day_added', models.DateField(blank=True, null=True)),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'ordering': ['product'],
                'verbose_name': 'Συστατικά Τιμολογίου   ',
            },
        ),
        migrations.CreateModel(
            name='PayOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_created', models.DateField(auto_now_add=True, verbose_name='Ημερομηνία')),
                ('date_expired', models.DateField(verbose_name='Ημερομηνία Εξόφλησης')),
                ('payment_method', models.CharField(choices=[('1', 'Μετρητά'), ('2', 'Τραπεζική Κατάθεση'), ('3', 'Πιστωτική Κάρτα'), ('4', 'Paypal')], default='3', max_length=1)),
                ('receipt', models.CharField(default='---', max_length=64, verbose_name='Απόδειξη')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Ποσό')),
                ('status', models.CharField(choices=[('a', 'Σε εξέλιξη'), ('b', 'Εισπράκτηκε'), ('c', 'Ακυρώθηκε')], default='a', max_length=1, verbose_name='Κατάσταση')),
            ],
            options={
                'verbose_name': 'Εντολές Πληρωμής',
            },
        ),
        migrations.CreateModel(
            name='PreOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('a', 'Active'), ('b', 'Used')], default='a', max_length=1)),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderNewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_buy', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Αγοράς')),
                ('discount_buy', models.IntegerField(default=0, verbose_name='Εκπτωση Τιμολογίου')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Λιανικής')),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('day_added', models.DateField(auto_now=True)),
                ('day_expire', models.DateField(auto_now=True)),
                ('send_status', models.BooleanField(default=False)),
                ('is_sended', models.CharField(choices=[('a', 'Ενεργό'), {'b', 'Στάλθηκε.'}], default='a', max_length=1)),
                ('print_status', models.BooleanField(default=False)),
                ('is_printed', models.CharField(choices=[('a', 'Ενεργό'), {'b', 'Εκτυπώθηκε.'}], default='a', max_length=1)),
                ('consume_to_order', models.BooleanField(default=False, verbose_name='Μετατροπή σε Τιμολόγιο.')),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderStatementItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderStatementNewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_buy', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Αγοράς')),
                ('discount_buy', models.IntegerField(default=0, verbose_name='Εκπτωση Τιμολογίου')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Λιανικής')),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseOrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=inventory_manager.models.upload_image, validators=[inventory_manager.models.validate_file])),
                ('is_first', models.BooleanField(default=True)),
                ('order_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.Order')),
            ],
        ),
    ]
