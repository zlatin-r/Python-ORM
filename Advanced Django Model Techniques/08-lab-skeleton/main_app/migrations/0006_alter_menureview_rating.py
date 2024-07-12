# Generated by Django 5.0.4 on 2024-07-12 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_menureview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menureview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
