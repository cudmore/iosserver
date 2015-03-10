#/bin/bash/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO.setmode(GPIO.BOARD)

#rotary encoder is attached to pins GPIO23 (16) and GPIO24 (18)
#wiring pi 4 and 5
rotaryPin1 = 23
rotaryPin2 = 24

GPIO.setup(rotaryPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rotaryPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:

	if(GPIO.input(rotaryPin1) ==1):
		print('Button 1 pressed')

	if(GPIO.input(rotaryPin2) == 0):
		print('Button 2 pressed')

GPIO.cleanup()
