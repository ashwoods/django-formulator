from setuptools import setup, find_packages
import re
import os
import sys

from formulator import get_version


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='django-formulator',
    version=get_version(),
    description='Core library for the formulator service',
    author='Ashley Camba Garrido',
    url='https://github.com/ashwoods/django-formulator',
    packages=get_packages('formulator'),
    package_data=get_package_data('formulator'),
    license='MIT')

