# Generated by Django 4.1.7 on 2023-03-13 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0009_transportationtype_transportation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ids', to='Trip.accommodationtype'),
        ),
    ]
