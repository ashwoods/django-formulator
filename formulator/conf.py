from django.conf import settings  # noqa
from appconf import AppConf  # noqa

from floppyforms import fields, widgets

# We want to get all the fields and widgets


class FormulatorConf(AppConf):

    WIDGETS = [(widget, '%s.%s' % (widgets.__name__, widget)) for widget in widgets.__all__]
    FIELDS = [(field, '%s.%s' % (fields.__name__, field)) for field in fields.__all__]
