# Generated by Django 4.1.7 on 2023-03-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0002_accommodationtype_activity_accommodation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.accommodationtype'),
        ),
    ]
