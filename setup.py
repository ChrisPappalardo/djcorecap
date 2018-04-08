# -*- coding: utf-8 -*-

'''
djcorecap/setup
---------------

setuptools setup file for the djcorecap package
'''


import os
from setuptools import find_packages, setup


with open('README') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'django>=1.8',
]

setup_requirements = []

test_requirements = []


setup(
    author='Chris Pappalardo',
    author_email='cpappala@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    description='Core app for Django projects that provides essential functions, tags, and enhanced Bootstrap-friendly templates.',
    install_requires=requirements,
    license="MIT license",
    long_description='%s\n\n%s' % (readme, history),
    include_package_data=True,
    keywords='djcorecap',
    name='djcorecap',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ChrisPappalardo/djcorecap',
    version='0.1.0',
    zip_safe=False,
)
