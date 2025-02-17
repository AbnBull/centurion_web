from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^elevation/(?P<lat>-?\d+(\.\d+)?)/(?P<lon>-?\d+(\.\d+)?)/$', views.get_elevation_ft, name='get_elevation'),
]
