from io import open
from setuptools import find_packages, setup


setup(
    name='django-formulator',
    description='A django library for creating dynamic django form classes.',
    author='Ashley Camba Garrido',
    author_email='ashwoods@gmail.com',
    url='https://github.com/ashwoods/django-formulator',
    download_url='https://pypi.python.org/pypi/django-formulator',
    packages=find_packages(exclude=('tests.*', 'tests', 'example')),
    license='BSD',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
     'django>=1.8',
     'django-model-utils',
     'django-appconf',
     'django-autoslug',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)

