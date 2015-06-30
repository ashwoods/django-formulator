from __future__ import print_function

SECRET_KEY = '!5myuh^d23p9$$lo5k$39x&ji!vceayg+wwt472!bgs$0!i3k4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


INSTALLED_APPS = [
    'formulator',
    'floppyforms',
]

ROOT_URLCONF = 'urls'

MIDDLEWARE_CLASSES = []
