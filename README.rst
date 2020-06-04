==============
geojson-length
==============


.. image:: https://img.shields.io/pypi/v/geojson-length.svg
        :target: https://pypi.python.org/pypi/geojson-length

.. image:: https://img.shields.io/travis/zaitra/geojson-length.svg
        :target: https://travis-ci.org/zaitra/geojson-length


Calculate the length of a GeoJSON LineString or MultiLineString


* Free software: MIT license
* Documentation: https://geojson-length.readthedocs.io.


Installation
------------

.. code::

  $ pip3 install geojson-length


Usage
------------

.. code:: python

  >>> from geojson_length import calculate_distance, Unit
  >>> from geojson import Feature, LineString

  >>> line = Feature(geometry=LineString([[19.6929931640625,48.953170117120976],[19.5556640625,48.99283383694351]]))
  >>> calculate_distance(line, Unit.meters)
  10979.098283583924

Note: You need to install python-geojson_ first or you can define GeoJSON as python dict:

.. _python-geojson: https://github.com/jazzband/geojson

.. code:: python

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

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

The idea was inspired by geojson-length_ package written in JS.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`geojson-length`: https://github.com/tyrasd/geojson-length
