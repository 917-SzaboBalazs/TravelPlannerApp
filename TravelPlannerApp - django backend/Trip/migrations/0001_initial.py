# Generated by Django 4.1.7 on 2023-03-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('accommodation', models.CharField(max_length=60)),
                ('budget', models.FloatField()),
                ('activities', models.CharField(max_length=120)),
                ('transportation', models.CharField(max_length=120)),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
