from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from datetime import timedelta
from .order import Order
from common.utilities.general_utilities import calculate_hash
from support.models import Box, WorldBorder

PICKUP_GENERATE_ATTRIBUTE_VERSION=1

class Pickup(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, default=Box.get_default_pk)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pickups')
    offset = models.DurationField(blank=False, null=False, default=timedelta)
    location = models.PointField(blank=False, null=False, srid=4326, default=Point(-95.9, 41.2))
    altitude_ft = models.FloatField(blank=False, null=False, default=0)
    country = models.ForeignKey('support.WorldBorder', on_delete=models.CASCADE, null=True, blank=True)
    saved_simulated_attribute_hash = models.CharField(max_length=16,blank=True,null=False)

    def __str__(self):
        return f'{self.box.name} pickup'

    def datetime(self):
        return self.order.datetime() + self.offset
    

    def simulated_attribute_hash(self):
        return calculate_hash(' '.join([
            f'{PICKUP_GENERATE_ATTRIBUTE_VERSION}',
            f'{self.location.x:.2f}',
            f'{self.location.y:.2f}',
            ]))

    def generate_attributes(self):

        # calculate country
        print(f'testing to see if {self.location.x} {self.location.y} is in a country')
        self.country = WorldBorder.objects.filter(mpoly__contains=self.location).first()
        print(f'we returned {self.country}')

        # update hash
        self.simulated_attribute_hash = self.simulated_attribute_hash()


    