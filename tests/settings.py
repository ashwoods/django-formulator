from __future__ import print_function

SECRET_KEY = '!5myuh^d23p9$$lo5k$39x&ji!vceayg+wwt472!bgs$0!i3k4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'formulator',
    'floppyforms',
    'crispy_forms',

]

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE_CLASSES = []

FORMULATOR_CRISPY_ENABLED = True

CRISPY_TEMPLATE_PACK = 'bootstrap'
