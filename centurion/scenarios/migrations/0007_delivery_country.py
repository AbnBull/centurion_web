# Generated by Django 5.0.3 on 2024-04-07 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0006_pickup_country'),
        ('support', '0002_worldborder'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='support.worldborder'),
        ),
    ]