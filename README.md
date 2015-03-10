###Rotary encoder in the Pi

####Follow this library  first, no interrupts  

> http://guy.carpenter.id.au/gaugette/2013/06/04/updating-to-wiringpi2-py/
> https://github.com/guyc/py-gaugette

- Install instructions are at end of github enter
- start to make symbolic links from Sites/ into one library location (Share across /usr/bin/python and /miniconda/bin/python  

		# 1) try this
		# http://guy.carpenter.id.au/gaugette/2013/06/04/updating-to-wiringpi2-py/
		# 2) wiring pi is a library where we directly import a .py file (e.g. it is not installed)
		# copy into directory i will use it in
		# pi@pi40 ~ $ sudo cp -R py-gaugette/gaugette/* Sites/iosserver/gaugette/
		#
		# run with 'sudo /usr/bin/python Sites/iosserver/gaugette.py
		#
		# IMPORTANT: libraries should be in
		# /usr/local/lib/python2.7/dist-packages/wiringpi2-1.0.10-py2.7-linux-armv6l.egg
		#
		# WORKS !!! 
		#
		# the above installed into /usr/bin/python but i am really using /home/pi/miniconda/
		# use this to install all packages
		# sudo ~/miniconda/bin/python setup.py install
		#
		# this is necc. because 'sudo is dumping me in /usr/bin/python
		# instead of /home/pi/miniconda ????
		#
		# now i have my egg here:
		# /home/pi/miniconda/lib/python2.7/site-packages/gaugette-1.2-py2.7.egg-info
		#
		# now when i run python with sudo i STILL need t specify the full path:
		# sudo /home/pi/miniconda/bin/python Sites/iosserver/gaugette.py

####Then try and get this c library compiled (with interrupts)

> http://theatticlight.net/posts/Reading-a-Rotary-Encoder-from-a-Raspberry-Pi/
> https://github.com/astine/rotaryencoder

compiling should look like this

> gcc -o mylib rotaryencoder.c -l wiringPi

i wrote my own setup.py but it does not work. expects lots of function headers like _init_

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

Look into swig (hard)
> http://www.swig.org

ctypes (easier)
> https://docs.python.org/2/library/ctypes.html

Following: http://karuppuswamy.com/wordpress/2012/01/28/how-to-use-c-library-in-python-generating-python-wrappers-for-c-library/

> makes rotaryencoder.o
> gcc -Wall -fPIC -c rotaryencoder.c
> makes rotaryencoder.so
> gcc -shared -Wl,-soname,libflags.so.1 -o rotaryencoder.so rotaryencoder.o
> 
This fixes digital read error (by using -l wiringPi)
> gcc -Wall -fPIC -l wiringPi -c rotaryencoder.c

Now I get 

