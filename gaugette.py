#/usr/bin/python

#using: http://guy.carpenter.id.au/gaugette/2013/01/14/rotary-encoder-library-for-the-raspberry-pi/
#github: https://github.com/guyc/py-gaugette
#download
# git clone https://github.com/guyc/py-gaugette
#install
# cd py-gaugette/
# sudo python setup.py install

#wait, py-gaugette has lots of dependencies as it does much more than just rotary_encoder
#there is a .sh script with all the installs
#see: https://github.com/the-raspberry-pi-guy/OLED
#but that did not work, python does not find 'import gaugette.rotary_encoder

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


rotaryPin1 = 5 #24
rotaryPin2 = 4 #23

import gaugette.rotary_encoder
import gaugette.switch
 
A_PIN  = 5 #9
B_PIN  = 4 #7
#SW_PIN = 8
 
#encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)

encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
print 'rotary encoder initialized with gaugette.rotary_encoder.RotaryEncoder.Worker'

#switch = gaugette.switch.Switch(SW_PIN)
last_state = None
 
while True:
    delta = encoder.get_delta()
    if delta!=0:
        print "rotate %d" % delta
 
    #sw_state = switch.get_state()
    #if sw_state != last_state:
    #    print "switch %d" % sw_state
    #    last_state = sw_state

