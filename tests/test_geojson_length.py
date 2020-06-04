#!/usr/bin/env python

"""Tests for `geojson_length` package."""

import pytest

from geojson_length import calculate_distance, Unit


# *** LineString ***


@pytest.fixture
def geojson_santiago_bernabeu():
    """
    Santiago Bernabéu Stadium has 105m
    """
    #
    return {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-3.688431680202484, 40.453537706073185],
                [-3.6885067820549016, 40.45259884887462],
            ],
        },
    }


@pytest.fixture
def geojson_wenceslas_square():
    """
    Wenceslas Square has width 60m
    """
    return {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [14.428870975971222, 50.080010634213316],
                [14.429552257061003, 50.08031528914452],
            ],
        },
    }


def test_length_sb(geojson_santiago_bernabeu):
    assert calculate_distance(
        geojson_santiago_bernabeu, unit=Unit.meters
    ) == pytest.approx(104.71, rel=1e-1)
    assert calculate_distance(
        geojson_santiago_bernabeu, unit=Unit.kilometers
    ) == pytest.approx(0.10, rel=1e-1)
    assert calculate_distance(
        geojson_santiago_bernabeu, unit=Unit.miles
    ) == pytest.approx(0.07, rel=1e-1)
    assert calculate_distance(
        geojson_santiago_bernabeu, unit=Unit.feet
    ) == pytest.approx(343.53, rel=1e-1)
    assert calculate_distance(
        geojson_santiago_bernabeu, unit=Unit.yards
    ) == pytest.approx(114.51, rel=1e-1)


def test_length_ws(geojson_wenceslas_square):
    assert calculate_distance(
        geojson_wenceslas_square, unit=Unit.meters
    ) == pytest.approx(59.32, rel=1e-1)
    assert calculate_distance(
        geojson_wenceslas_square, unit=Unit.kilometers
    ) == pytest.approx(0.06, rel=1e-1)
    assert calculate_distance(
        geojson_wenceslas_square, unit=Unit.miles
    ) == pytest.approx(0.04, rel=1e-1)
    assert calculate_distance(
        geojson_wenceslas_square, unit=Unit.feet
    ) == pytest.approx(194.61, rel=1e-1)
    assert calculate_distance(
        geojson_wenceslas_square, unit=Unit.yards
    ) == pytest.approx(64.87, rel=1e-1)


# *** MultiLineString ***


@pytest.fixture
def geojson_multilinestring():
    return {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "MultiLineString",
            "coordinates": [
                [
                    [19.54193115234375, 49.03786794532644],
                    [19.7698974609375, 49.14937676724421],
                    [19.82757568359375, 49.01085236926211],
                    [20.0225830078125, 48.96038404976431],
                ],
                [
                    [19.6929931640625, 48.953170117120976],
                    [19.5556640625, 48.99283383694351],
                ],
            ],
        },
    }


def test_length_multiline(geojson_multilinestring):
    assert calculate_distance(
        geojson_multilinestring, unit=Unit.meters
    ) == pytest.approx(63002.59, rel=1e-1)
    assert calculate_distance(
        geojson_multilinestring, unit=Unit.kilometers
    ) == pytest.approx(63, rel=1e-1)
    assert calculate_distance(
        geojson_multilinestring, unit=Unit.miles
    ) == pytest.approx(39.15, rel=1e-1)
    assert calculate_distance(geojson_multilinestring, unit=Unit.feet) == pytest.approx(
        206701.4, rel=1e-1
    )
    assert calculate_distance(
        geojson_multilinestring, unit=Unit.yards
    ) == pytest.approx(68900.47, rel=1e-1)
