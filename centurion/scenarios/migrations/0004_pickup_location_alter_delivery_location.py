# Generated by Django 5.0.3 on 2024-04-03 20:26

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0003_delivery_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-95.9, 41.2), srid=4326),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-86.6, 34.7), srid=4326),
        ),
    ]
