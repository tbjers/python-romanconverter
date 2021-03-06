# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='romanconverter',
    version='0.1.0',
    description='Package to convert Roman numerals.',
    long_description=readme,
    author='Torgny Bjers',
    author_email='torgny@bjers.org',
    url='https://github.com/tbjers/python-romanconverter',
    license=license,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dec2roman=scripts.dec2roman:cli
    '''
)
