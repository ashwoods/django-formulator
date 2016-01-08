from django.conf import settings  # noqa


from appconf import AppConf  # noqa
import floppyforms as forms


class FormulatorConf(AppConf):

    WIDGETS = [('%s.%s' % (forms.widgets.__name__, widget), widget) for widget in forms.widgets.__all__]
    FIELDS = [('%s.%s' % (forms.fields.__name__, field), field) for field in forms.fields.__all__]
    BASE_MODEL = None
    CRISPY_ENABLED = False
    DEFAULT_FORM_LIBRARY = forms
    DEFAULT_FORM_CLASS = DEFAULT_FORM_LIBRARY.Form
