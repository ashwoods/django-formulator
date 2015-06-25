import os
import re
import codecs
from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-formulator',
    version=find_version("formulator", "__init__.py"),
    description='Core library for the formulator service',
    author='Ashley Camba Garrido',
    url='https://github.com/ashwoods/django-formulator',
    packages=['formulator'],
    license='MIT',
    install_requires=[
     'django>=1.7',
     'django-positions',
     'django-model-utils',
     'django-appconf',
     'django-autoslug',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)

