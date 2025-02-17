from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def get_elevation(request, lat, lon, meters_flag):
    # Convert the latitude and longitude to a Point geometry
    point = f'ST_SetSRID(ST_MakePoint({lon}, {lat}), 4326)'

    # Construct the SQL query to extract the elevation value
    sql = f'''
        SELECT ST_Value(raster, {point})
        FROM support_elevation
        WHERE ST_Intersects(raster, {point});
    '''

    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()

    # Return the elevation value as a JSON response
    if result:
        if not meters_flag:
            elevation = result[0] * 3.281
        else:
            elevation = result[0]
        return JsonResponse({'elevation': elevation})
    else:
        return JsonResponse({'error': 'Elevation data not available for this location'}, status=404)


def get_elevation_ft(request, lat, lon):
    return get_elevation(request, lat, lon, False)


def get_elevation_m(request, lat, lon):
    return get_elevation(request, lat, lon, True)
    
    

