#!/usr/bin/env python
# -*- coding:utf-8 -*-

# THIS DOES NOT WORK !!!!!

from distutils.core import setup, Extension

rotary_mod = Extension('myrotaryencoder',
                    include_dirs = ['.'],
                    libraries = ['wiringPi'],
                    sources = ['rotaryencoder.c'])

setup (name = 'myrotaryencoder',
       version = '1.0',
       description = 'Python library to interface with rotary encoder',
       ext_modules = [rotary_mod])
       

#dht_mod = Extension('dhtreader',
#                    include_dirs = ['.'],
#                    libraries = ['bcm2835'],
#                    sources = ['dhtreader.c'])
#
#setup (name = 'dhtreader',
#       version = '1.0',
#       description = 'Python library to interface with dht sensors',
#       ext_modules = [dht_mod])