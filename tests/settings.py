# -*- coding: utf-8 -*-
SECRET_KEY = '!5myuh^d23p9$$lo5k$39x&ji!vceayg+wwt472!bgs$0!i3k4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'formulator',
    'crispy_forms',

]

ROOT_URLCONF = 'tests.urls'
MIDDLEWARE_CLASSES = []
CRISPY_TEMPLATE_PACK = 'bootstrap'
