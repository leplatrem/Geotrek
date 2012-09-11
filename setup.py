#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

test_requirements = [
    'factory_boy == 1.1.5',
]


setup(
    name='caminae',
    version='1.0.dev0',
    author='Makina Corpus',
    author_email='geobi@makina-corpus.com',
    url='http://makina-corpus.com',
    description="Caminae",
    long_description=open(os.path.join(here, 'README.rst')).read(),
    install_requires = [
        'django',  # pinned by buildout
        'South == 0.7.5',
        'psycopg2 == 2.4.1',
        'GDAL == 1.9.1',
        # 'pyshp == 1.1.4',
        'django-shapes == 0.2.0',
        'django-modeltranslation == 0.3.3',
        'django-floppyforms == 1.0',
        'django-crispy-forms == 1.1.4',
        'django-compressor == 1.2',
        'Pillow == 1.7.7',
        'easy-thumbnails == 1.1',
        'django-appypod == 0.0.1',
        'django-leaflet',   # pinned by buildout
        'django-geojson',   # pinned by buildout
        'django-filter',   # pinned by buildout
        'django-extended-choices',  # pinned by buildout
        'django-tinymce',  # pinned by buildout
    ] + test_requirements,
    tests_requires = test_requirements,
    packages=find_packages(),
    classifiers  = ['Natural Language :: English',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.5'],
)
