# Generated by Django 5.0.4 on 2024-07-08 08:33

import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_userprofile_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', main_app.models.StudentIDField(validators=[main_app.models.StudentIDField.validate_student_id])),
            ],
        ),
    ]
