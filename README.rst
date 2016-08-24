django-formulator
=================

.. image:: https://img.shields.io/pypi/v/django-formulator.svg
   :alt: PyPi page
   :target: https://pypi.python.org/pypi/django-formulator

.. image:: https://img.shields.io/travis/ashwoods/django-formulator.svg
    :alt: Travis CI Status
    :target: https://travis-ci.org/ashwoods/django-formulator

.. image:: https://coveralls.io/repos/ashwoods/django-formulator/badge.svg?branch=master&service=github 
   :target: https://coveralls.io/github/ashwoods/django-formulator?branch=master
   :alt: Coverage status

.. image:: https://codeclimate.com/repos/57bd6a42a1089006f70021b6/badges/877b308ef3fc32e938e7/gpa.svg
   :target: https://codeclimate.com/repos/57bd6a42a1089006f70021b6/feed
   :alt: Code Climate

.. image:: https://api.codacy.com/project/badge/Grade/a6114b28442f4412b0959afc5f7df54d
   :target: https://www.codacy.com/app/ashwoods/django-formulator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ashwoods/django-formulator&amp;utm_campaign=Badge_Grade
   :alt: Codacy

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
