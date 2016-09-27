#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    version='0.0.2',
    description='ShipHawk API Client for Python',
    author='Douglas Treadwell',
    author_email='douglas.treadwell@gmail.com',
    url='https://github.com/Distributd/shiphawk-client-python',
    packages=['shiphawk'],
    install_requires=[
        'requests[security] >= 2.11.1'
    ]
)
