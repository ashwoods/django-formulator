import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='django-formulator',
    version=__import__('formulator').__version__,
    author='Ashley Camba Garrido',
    author_email='ashwoods@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    tests_require=['coverage', 'flake8'],
    url='',
    license='BSD License',
    description=u' '.join(__import__('formulator').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
)
