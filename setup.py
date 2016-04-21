#!/usr/bin/env python

from setuptools import find_packages, setup

# setup the project
setup(
    name='cmsplugin-forms-builder-08eins-custom',
    version='2.0.0',
    description='django-cms plugin for cmsplugin-forms-builder',
    long_description=open('README.md').read(),
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='https://github.com/08EINS/cmsplugin-forms-builder/',
    packages=find_packages(exclude=["tests", ]),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    find_links=[

    ],
    install_requires=[
        'Django',
        'django-cms',
        'django-forms-builder-08eins-custom',
    ],
    zip_safe=False
)
