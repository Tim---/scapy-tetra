#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scapy_tetra',
    version='0.1.0',
    description='TETRA dissector for Scapy',
    url='https://github.com/Tim---/scapy-tetra',
    author='Timothée COCAULT',
    author_email='timothee.cocault@gmail.com',
    license='GPLv2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Topic :: Communications :: Ham Radio',
    ],
    keywords='scapy tetra',
    packages=find_packages(),
    install_requires=['scapy']
)
