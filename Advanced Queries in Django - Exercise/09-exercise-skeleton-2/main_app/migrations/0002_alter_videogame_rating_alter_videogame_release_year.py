# Generated by Django 5.0.4 on 2024-07-28 10:24

import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[validators.rating_validator]),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='release_year',
            field=models.PositiveIntegerField(validators=[validators.release_year_validator]),
        ),
    ]
