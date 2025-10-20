# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


class DynamicFormsConfig(AppConfig):
    name = 'formulator'
    verbose_name = _("Formulator")
    
    def ready(self):
        # Import checks to register them with Django's check framework
        from formulator import checks  # noqa
