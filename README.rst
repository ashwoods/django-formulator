django-formulator
=================

.. image:: https://img.shields.io/pypi/v/django-formulator.svg
   :alt: PyPi page
   :target: https://pypi.python.org/pypi/django-formulator

.. image:: https://img.shields.io/travis/ashwoods/django-formulator.svg
    :alt: Travis CI Status
    :target: https://travis-ci.org/ashwoods/django-formulator

.. image:: https://img.shields.io/coveralls/ashwoods/django-formulator/master.svg
   :alt: Coverage status
   :target: https://coveralls.io/r/ashwoods/django-formulator

.. image:: https://readthedocs.org/projects/django-formulator/badge/?version=latest&style=flat
   :alt: ReadTheDocs
   :target: http://django-formulator.readthedocs.org/en/latest/

.. image:: https://img.shields.io/pypi/l/django-formulator.svg
   :alt: License BSD



Welcome to the documentation for django-formulator!


This software is in design/alpha stage, and the docs are incomplete!


Abstract
-----------------------------------

Formulator is not a survey app. It just saves django form definitions in the db,
that developers can use in their views. In other words you get a dynamic subclass of
django BaseForm.

You can provide your own class base to handle the saving part. This makes it really
easy to define forms (or in a way, models) for data that will be saved in NoSQL dbs.


Installation
------------

::

    pip install django-formulator


Usage
-----------------------------------

:Todo


Running the Tests
------------------------------------

You can run the tests with via::

    make test
