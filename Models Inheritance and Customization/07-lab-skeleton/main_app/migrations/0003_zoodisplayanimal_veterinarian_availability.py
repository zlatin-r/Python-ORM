# Generated by Django 5.0.4 on 2024-07-07 12:20

import main_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_veterinarian_zookeeper'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZooDisplayAnimal',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.animal',),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='availability',
            field=main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True),
        ),
    ]
