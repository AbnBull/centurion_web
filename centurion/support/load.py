#from .models import Elevation
from django.contrib.gis.gdal import GDALRaster
from django.contrib.gis.utils import LayerMapping
import os
from pathlib import Path
from .models import WorldBorder

#def import_elevation_data():
#
#    data_path =  Path(__file__).resolve().parent.parent.parent / "data" / "low_res_resampled_reprojected_ETOPO.tif"
#    # import raster
#    elevation_raster = GDALRaster(data_path, write=True)
#    print("Raster object created successfully.")
#    print(f"Raster size: {elevation_raster.width}x{elevation_raster.height}")
#    print(f"Number of bands: {elevation_raster.bands}")
#    print(f"SRID: {elevation_raster.srs.srid if elevation_raster.srs else 'None'}")
#
#    # Create elevation object
#    new_elevation_object = Elevation.objects.create(raster=elevation_raster,name="ETOPO 2022")
#    new_elevation_object.save()
#    print('import complete!')

# World Border Import
world_mapping = {
    "fips": "FIPS",
    "iso2": "ISO2",
    "iso3": "ISO3",
    "un": "UN",
    "name": "NAME",
    "area": "AREA",
    "pop2005": "POP2005",
    "region": "REGION",
    "subregion": "SUBREGION",
    "lon": "LON",
    "lat": "LAT",
    "mpoly": "MULTIPOLYGON",
}

world_shp = Path(__file__).resolve().parent.parent.parent / "data" / "TM_WORLD_BORDERS-0.3.shp"

def import_world_border_data(verbose=True):
    print(f'importing {world_shp}')
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
    print(f'done importing')