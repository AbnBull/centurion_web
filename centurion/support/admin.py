from django.contrib.gis import admin
from .models import Box, WorldBorder


admin.site.register(Box)
admin.site.register(WorldBorder)