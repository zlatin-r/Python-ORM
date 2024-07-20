# Generated by Django 5.0.4 on 2024-07-20 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(2)])),
                ('birth_date', models.DateField(default='1900-01-01')),
                ('nationality', models.CharField(default='Unknown', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(2)])),
                ('birth_date', models.DateField(default='1900-01-01')),
                ('nationality', models.CharField(default='Unknown', max_length=50)),
                ('years_of_experience', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('actors', models.ManyToManyField(related_name='actor_movies', to='main_app.actor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
