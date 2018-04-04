# Generated by Django 2.0 on 2018-03-18 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20180307_0853'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_value', models.PositiveIntegerField(default=0)),
                ('shipping_value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='coupons',
            name='cart_total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='coupons',
            name='categories',
            field=models.ManyToManyField(to='products.CategorySite'),
        ),
        migrations.AddField(
            model_name='coupons',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupons',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupons',
            name='discount_percent',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupons',
            name='discount_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='coupons',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Country'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='coupons',
            field=models.ManyToManyField(to='cart.Coupons'),
        ),
    ]
