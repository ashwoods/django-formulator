
from django.conf import settings  # noqa
from django.utils.encoding import python_2_unicode_compatible

from appconf import AppConf  # noqa
from model_utils.models import TimeStampedModel
from floppyforms import fields, widgets
# We want to get all the fields and widgets


@python_2_unicode_compatible
class BaseModel(TimeStampedModel):

    def __str__(self):
        return '<%s:%s>' % (self.__cls__.name, self.pk)


class FormulatorConf(AppConf):

    WIDGETS = [(widget, '%s.%s' % (widgets.__name__, widget)) for widget in widgets.__all__]
    FIELDS = [(field, '%s.%s' % (fields.__name__, field)) for field in fields.__all__]
    BASE_MODEL = BaseModel
    CRISPY_ENABLED = False
    FLOPPY_ENABLED = False


