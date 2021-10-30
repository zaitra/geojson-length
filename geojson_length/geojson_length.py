from enum import Enum
from typing import Optional
from geojson_length.exc import GeojsonLengthException

import geopy.distance


class Unit(Enum):
    meters = "m"
    kilometers = "km"
    feet = "ft"
    miles = "mi"
    yards = "yd"


def distance_between_two_points(
    point1: list, point2: list, unit: Unit = Unit.meters
) -> Optional[float]:
    """
    Calculate distance between two points
    :param point1: [longitude, latitude]
    :param point2: [longitude, latitude]
    :param unit: unit of result
    :return: distance between two points
    """

    # GeoPy needs lat, lon
    point1 = tuple(reversed(point1[:2]))
    point2 = tuple(reversed(point2[:2]))

    if unit == Unit.meters:
        return geopy.distance.distance(point1, point2).meters
    elif unit == Unit.kilometers:
        return geopy.distance.distance(point1, point2).kilometers
    elif unit == Unit.feet:
        return geopy.distance.distance(point1, point2).feet
    elif unit == Unit.miles:
        return geopy.distance.distance(point1, point2).miles
    elif unit == Unit.yards:
        # one yard is 3 feet
        # source: https://www.metric-conversions.org/length/yards-conversion.htm
        return geopy.distance.distance(point1, point2).feet / 3


def calculate_line_string(
    coordinates: list, unit: Unit = Unit.meters
) -> Optional[float]:
    """
    Calculate distance of LineString or MultiLineString GeoJSON
    :param coordinates: 2D array of points e.g [[49.0, 15.0], [50.0, 12.3]]
    :param unit: Unit of the result
    :return: distance in preferred units
    """
    if len(coordinates) < 2:
        return 0

    distance = 0
    for i in range(1, len(coordinates)):
        distance += distance_between_two_points(
            coordinates[i - 1], coordinates[i], unit=unit
        )

    return distance


def calculate_distance(geojson, unit: Unit = Unit.meters) -> Optional[float]:
    """
    Calculate distance of LineString or MultiLineString GeoJSON.
    Raises geojson_length.exc.GeojsonLengthException if input GeoJSON is invalid.
    :param geojson: GeoJSON feature of type LineString or MultiLineString
    :param unit: Unit of the result
    :return: distance in preferred units
    """
    try:
        geometry = geojson.get("geometry", None)
    except AttributeError:
        raise GeojsonLengthException(
            "Invalid GeoJSON provided. Should be geojson.geometry.LineString,"
            " geojson.geometry.MultiLineString or dict"
        )

    if not geometry:
        raise GeojsonLengthException("Provided GeoJSON object has no geometry field")

    coordinates = geometry.get("coordinates", None)

    if not coordinates:
        raise GeojsonLengthException(
            "Provided GeoJSON object has no coordinates specified in geometry field"
        )

    geometry_type = geometry.get("type", None)

    if not geometry_type:
        raise GeojsonLengthException(
            "Provided GeoJSON object has no type specified in geometry field"
        )

    if geometry_type == "LineString":
        return calculate_line_string(coordinates, unit)
    elif geometry_type == "MultiLineString":
        distance = 0
        for line in coordinates:
            distance += calculate_line_string(line, unit)
        return distance
    else:
        return None
