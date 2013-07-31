import os

TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests')

COMPRESS_CACHE_BACKEND = 'locmem://'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'formulator',
    'floppyforms',
]

STATIC_URL = '/static/'

SECRET_KEY = 'this-key-is-not-very-secret'
TEMPLATE_DIRS = (
    # Specifically choose a name that will not be considered
    # by app_directories loader, to make sure each test uses
    # a specific template without considering the others.
    # os.path.join(TEST_DIR, 'test_templates'),
)

TEST_RUNNER = 'discover_runner.DiscoverRunner'
