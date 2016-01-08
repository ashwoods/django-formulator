from django.conf import settings  # noqa
from django.utils.encoding import python_2_unicode_compatible

from appconf import AppConf  # noqa
from model_utils.models import TimeStampedModel


import floppyforms as forms


@python_2_unicode_compatible
class BaseModel(TimeStampedModel):

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.pk)

    class Meta:
        abstract=True


class FormulatorConf(AppConf):

    WIDGETS = [('%s.%s' % (forms.widgets.__name__, widget), widget) for widget in forms.widgets.__all__]
    FIELDS = [('%s.%s' % (forms.fields.__name__, field), field) for field in forms.fields.__all__]
    BASE_MODEL = BaseModel
    CRISPY_ENABLED = False
    DEFAULT_FORM_LIBRARY = forms
    DEFAULT_FORM_CLASS = DEFAULT_FORM_LIBRARY.Form
