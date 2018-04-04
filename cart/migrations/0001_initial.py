# Generated by Django 2.0 on 2018-02-27 07:04

import cart.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20180227_0904'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('id_session', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[cart.models.validate_positive_decimal])),
                ('is_complete', models.BooleanField(default=False)),
                ('payment_method', models.CharField(choices=[('1', 'Μετρητά'), ('2', 'Τραπεζική Κατάθεση'), ('3', 'Πιστωτική Κάρτα'), ('4', 'Paypal')], default='a', max_length=1)),
            ],
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_session', models.CharField(max_length=50)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[cart.models.validate_positive_decimal])),
                ('price_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[cart.models.validate_positive_decimal])),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[cart.models.validate_positive_decimal])),
                ('characteristic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.SizeAttribute')),
                ('order_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('product_related', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[cart.models.validate_positive_decimal])),
                ('active_cost', models.BooleanField(default=True)),
                ('active_minimum_cost', models.DecimalField(decimal_places=2, default=40, max_digits=6, validators=[cart.models.validate_positive_decimal])),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Country')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='shipping_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Shipping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]