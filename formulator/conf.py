# -*- coding: utf-8 -*-
from django.conf import settings  # noqa

from appconf import AppConf  # noqa
from . import fields

ALL_FIELDS = [getattr(fields, field) for field in fields.__all__]


class FormulatorConf(AppConf):

    WIDGETS = []
    FIELDS = [
        ('%s.%s' % (field.__module__, field.__name__), field.__doc__) for field
        in ALL_FIELDS
    ]
    ABSTRACT_BASE_MODEL = 'django.db.models.Model'
    FIELDS_MODULE = 'django.forms'
    FORM_CLASS = 'django.forms.Form'
    SIMPLIFY_ADMIN = True
