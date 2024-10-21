# Generated by Django 5.0.7 on 2024-09-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]