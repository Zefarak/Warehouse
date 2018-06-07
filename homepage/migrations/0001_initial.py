# Generated by Django 2.0 on 2018-06-07 11:07

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=homepage.models.upload_banner, validators=[homepage.models.validate_size])),
                ('href', models.URLField(blank=True, null=True)),
                ('new_window', models.BooleanField(default=False)),
                ('big_banner', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FirstPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to=homepage.models.upload_location, validators=[homepage.models.validate_size])),
                ('meta_description', models.CharField(max_length=160)),
                ('meta_keywords', models.CharField(max_length=160)),
            ],
        ),
    ]
