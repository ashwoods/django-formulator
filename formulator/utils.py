# -*- coding: utf-8 -*-

import importlib

from autoslug.settings import slugify as default_slugify


def slugify(value):
    return default_slugify(value).replace('-', '_')


def import_class(cls):
    module_name, class_name = cls.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)
