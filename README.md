# geojson-length

[![Build](https://github.com/zaitra/geojson-length/actions/workflows/release.yml/badge.svg)](https://github.com/zaitra/geojson-length/actions/workflows/release.yml) [![Pypi](https://img.shields.io/pypi/v/geojson-length.svg)](https://pypi.python.org/pypi/geojson-length)


Calculate the length of a GeoJSON LineString or MultiLineString


## Installation
------------

```
$ pip3 install geojson-length
```

## Usage
------------

```python
  >>> from geojson_length import calculate_distance, Unit
  >>> from geojson import Feature, LineString

  >>> line = Feature(geometry=LineString([[19.6929931640625,48.953170117120976],[19.5556640625,48.99283383694351]]))
  >>> calculate_distance(line, Unit.meters)
  10979.098283583924
```

> Note: You need to install [python-geojson](https://github.com/jazzband/geojson) first or you can define GeoJSON as python dict:

```python
    line = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            19.6929931640625,
            48.953170117120976
          ],
          [
            19.5556640625,
            48.99283383694351
          ]
        ]
      }
    }
```

## Run test suite

1. `$ pip install pytest`
2. `$ poetry run pytest --color=yes --verbose --showlocals tests`


> You may need to run `poetry install` first.


## Credits
-------

This package was created with Cookiecutter_ and the [audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.

The idea was inspired by [geojson-length](https://github.com/tyrasd/geojson-length) package written in JS.

## License

Free software: MIT license
