from math import atan2, asin, acos, sin, cos, sqrt
from .geospatial_utilities import intermediate_point
import datetime

RADIUS_EARTH_NM = 3443.92
DEGREES_TO_RADIANS = .01745
E2 = 0.00669437999014
DRONE_FLIGHT_ALTITUDE_NM = 5
DRONE_ASCENSION_DESCENSION_SECONDS=60

# From Converting between ECEF and Geodetic coordinates, D. Rose - November 2014
def convert_ECEF_to_geodetic(r1):

    a = RADIUS_EARTH_NM
    f = 0.00335281066

    # do the conversion
    x = r1[0]
    y = r1[1]
    z = r1[2]

    # derived constants
    b = a - f * a
    clambda = atan2(y, x)
    p = sqrt(x * x + y * y)
    h_old = 0 # first guess is 0 altitude
    theta = atan2(z, p * (1-E2))
    cs = cos(theta)
    sn = sin(theta)
    n = (a * a) / sqrt((a * cs) ** 2 + (b * sn) ** 2)
    h = p / cs - n
    while (h - h_old) > 1.0e-6:
        h_old = h
        theta = atan2(z, p * (1-E2 * n / (n + h)))
        cs = cos(theta)
        sn = sin(theta)
        n = (a * a) / sqrt((a * cs) ** 2 + (b * sn) ** 2)
        h = p / cs - n
    
    return  theta/DEGREES_TO_RADIANS, clambda/DEGREES_TO_RADIANS, h


# From Converting between ECEF and Geodetic coordinates, D. Rose - November 2014
def convert_geodetic_to_ECEF(lat_degrees, lon_degrees, alt_nm):

    # conversions
    lat = lat_degrees  * DEGREES_TO_RADIANS
    lon = lon_degrees * DEGREES_TO_RADIANS

    # ijk calcs
    cos_lat = cos(lat)
    sin_lat = sin(lat)
    n = RADIUS_EARTH_NM / sqrt(1 - E2 * sin_lat * sin_lat)
    iprime = (n + alt_nm) * cos_lat * cos(lon)
    jprime = (n + alt_nm) * cos_lat * sin(lon)
    kprime = (n * (1 - E2) + alt_nm) * sin_lat

    # return
    return [iprime, jprime, kprime]

def greenwich_sidereal_time(datetime_to_convert):

    # get the julian day start
    julian_day_0h0m = 367 * datetime_to_convert.year - int((7 / 4) * (datetime_to_convert.year + int((datetime_to_convert.month + 9) / 12))) + int(275 * datetime_to_convert.month / 9) + datetime_to_convert.day + 1721013.5
    print(f'j0={julian_day_0h0m}')
    # calculate month start
    no_time = datetime.datetime(datetime_to_convert.year, datetime_to_convert.month, datetime_to_convert.day) 
    dif_of_datetime = datetime_to_convert - no_time
    ut_dec = dif_of_datetime.total_seconds()/datetime.timedelta(days=1).total_seconds()

    # calc julian centuries
    julian_centuries_j2000 = (julian_day_0h0m - 2451545) / 36525
    print(f't0={julian_centuries_j2000}')

    # get theta
    theta_g0 = 100.4606184 + 36000.77004 * julian_centuries_j2000 + 0.000387933 * julian_centuries_j2000 ** 2 - 0.00000002583 * julian_centuries_j2000 ** 3

    # finish up
    return (theta_g0 + 360.98564724 * ut_dec) % 360


def generate_drone_seperation_point_and_timedelta(start_point, end_point, end_timedelta):
    
    # check on valid entries
    if end_timedelta.total_seconds()<=DRONE_ASCENSION_DESCENSION_SECONDS: # 60 seconds needed to ascend and descend
        return None, None
    if start_point == end_point:
        return None, None
    
    # calc flight duration
    flight_duration_seconds = end_timedelta.total_seconds()

    # seperation happens at 1/3 path (after boost phase)
    seperation_timedelta = datetime.timedelta(seconds=(flight_duration_seconds-DRONE_ASCENSION_DESCENSION_SECONDS)/3+DRONE_ASCENSION_DESCENSION_SECONDS/2)

    # calculate new point
    fraction = 0.333333
    return_point = intermediate_point(start_point, end_point, fraction)
    print(f'!!!!return point in gen drone sep point is {return_point} and start is {start_point} and end is {end_point}')

    # return
    return return_point, seperation_timedelta

    
def generate_drone_path(start_point, start_altitude, end_points, end_altitudes, end_timedeltas):

    # initialize return paths
    return_paths = []

    # validate end points
    if len(end_points) <= 0:
        return return_paths

    print(f'start point in generate drone path is {start_point} and end points are {end_points}')
    # generate single first path to seperation point
    seperation_end_point = end_points[0]
    seperation_end_point_time_delta = end_timedeltas[0]

    if seperation_end_point != start_point and seperation_end_point_time_delta.total_seconds() > DRONE_ASCENSION_DESCENSION_SECONDS:
        seperation_point, seperation_timedelta = generate_drone_seperation_point_and_timedelta(start_point, seperation_end_point, seperation_end_point_time_delta)
        first_path = [
            (start_point, start_altitude, datetime.timedelta(seconds=0)),
            (start_point, DRONE_FLIGHT_ALTITUDE_NM, datetime.timedelta(seconds=DRONE_ASCENSION_DESCENSION_SECONDS/2)),
            (seperation_point, DRONE_FLIGHT_ALTITUDE_NM, seperation_timedelta)
        ]
        return_paths.append(first_path)

    # generate MIRV paths
    for end_point, end_altitude, end_timedelta in zip(end_points, end_altitudes, end_timedeltas):
        if start_point != end_point and end_timedelta.total_seconds() > DRONE_ASCENSION_DESCENSION_SECONDS:
            new_path = [
                (seperation_point, DRONE_FLIGHT_ALTITUDE_NM, seperation_timedelta),
                (end_point, DRONE_FLIGHT_ALTITUDE_NM, end_timedelta-datetime.timedelta(seconds=DRONE_ASCENSION_DESCENSION_SECONDS/2)),
                (end_point, end_altitude, end_timedelta),
            ]
            return_paths.append(new_path)

    # return constructed paths
    print(f'return paths in generate drone path is {return_paths}')
    return return_paths

    

    
    