#/usr/bin/python

#record usb video AND roatary encoder at same time

import time
import datetime

#
#video
import numpy as np
import cv2

# initialize camera
cap = cv2.VideoCapture(0)
if cap is None:
    print 'Warning: unable to access camera'

# number of frames to acquire
numFrames = 30
currFrame = 0

#
# initialize rotary encoder
import gaugette.rotary_encoder
import gaugette.switch

A_PIN  = 5 #24
B_PIN  = 4 #23

encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
print 'rotary encoder initialized with gaugette.rotary_encoder.RotaryEncoder.Worker', A_PIN, B_PIN

#
# output file
iosServerPath = '/home/pi/Sites/iosserver/'
logFileTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
logFileName = iosServerPath + logFileTime + '.txt'
logFile = open(logFileName, 'w')
logFile.write('log file started at ' + logFileTime)

# BEGIN
print 'starting capture of ' + str(numFrames) + ' frames.'

while(cap.isOpened()):
    currTime = time.time() # each step through loop has a single time, Time in seconds since the epoch
    
    try:
        delta = encoder.get_delta()
        if delta!=0:
            #print currTime, "\trotate %d" % delta
            logFile.write('%f\t%d\n' % (currTime, delta))
        ret, frame = cap.read()
        if ret==True:
            #flip frame
            #frame = cv2.flip(frame,0)

            #print frame.shape

            # write the flipped frame
            try:
                #out.write(frame)
                #cv2.SaveImage('file' + str(currFrame) + '.tif', frame)
                logFile.write('%f\tframe=%d\n' % (currTime, currFrame))
                cv2.imwrite('Sites/iosserver/images/image' + str(currFrame) + '.tif', frame)
            except:
                print 'Error in out.write() OR user hit ctrl-c'
                break

            currFrame += 1
            #if (currFrame > numFrames):
            #    print 'finished ' + str(numFrames) + ' frames.'
            #    break
    
        else:
            break

    except KeyboardInterrupt:
        print 'user hit ctrl-c'
        print 'frames=' + str(currFrame)
        break

# Release camera
cap.release()
logFile.close()