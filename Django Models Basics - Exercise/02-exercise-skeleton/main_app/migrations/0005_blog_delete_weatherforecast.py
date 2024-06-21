# Generated by Django 5.0.4 on 2024-06-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_weatherforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('author', models.CharField(max_length=35)),
            ],
        ),
        migrations.DeleteModel(
            name='WeatherForecast',
        ),
    ]