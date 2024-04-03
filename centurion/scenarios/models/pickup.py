from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from .order import Order
from support.models import Box

class Pickup(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, default=Box.get_default_pk)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pickups')
    offset = models.DurationField(blank=False, null=False)
    location = models.PointField(blank=False, null=False, srid=4326, default=Point(-95.9, 41.2))
    altitude_ft = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.box.name} pickup'

    def datetime(self):
        return self.order.datetime() + self.offset