# Generated by Django 2.0.2 on 2018-03-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_coupon_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='final_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]