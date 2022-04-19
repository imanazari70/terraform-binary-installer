#!/usr/bin/env python

from setuptools import setup

setup(
    name='terraform-binary-installer',
    version='1.0.3',
    description='Python wrapper for install terraform version corresponding to package version.',
    author='Iman Azari',
    author_email='azari@mahsan.co',
    url='',
    packages=['terraform_binary_installer'],
    scripts=['scripts/terraform']
)
